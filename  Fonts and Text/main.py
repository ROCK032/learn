import pygame


# Функция для выбора доступного шрифта из списка предпочтений
def make_font(fonts, size):
    available = pygame.font.get_fonts()  # Получаем список доступных шрифтов
    choices = map(lambda x: x.lower().replace(' ', ''),
                  fonts)  # Приводим названия шрифтов к нижнему регистру без пробелов
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)  # Возвращаем первый найденный шрифт
    return pygame.font.Font(None, size)  # Если ни один не найден, используем системный шрифт


# Кэш для хранения загруженных шрифтов
_cached_fonts = {}


def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)  # Создаём ключ для кэша
    if key not in _cached_fonts:
        _cached_fonts[key] = make_font(font_preferences, size)  # Если шрифт не в кэше, загружаем его
    return _cached_fonts[key]


# Кэш для хранения рендеренного текста
_cached_text = {}


def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))  # Создаём ключ для кэша текста
    if key not in _cached_text:
        font = get_font(fonts, size)  # Получаем шрифт
        _cached_text[key] = font.render(text, True, color)  # Рендерим текст и сохраняем в кэше
    return _cached_text[key]


# Инициализация PyGame
pygame.init()
screen = pygame.display.set_mode((640, 480))  # Создаём окно
clock = pygame.time.Clock()  # Создаём объект Clock для управления FPS

done = False  # Флаг выхода из цикла

# Список предпочтительных шрифтов
font_preferences = [
    "Bizarre-Ass Font Sans Serif",  # Маловероятный шрифт (демонстрация поиска альтернатив)
    "They definitely dont have this installed Gothic",  # Ещё один нереальный вариант
    "Papyrus",  # Реальный шрифт, но не везде установлен
    "Comic Sans MS"  # Популярный шрифт, часто установлен по умолчанию
]

# Создаём текст с заданными параметрами
text = create_text("Hello, World", font_preferences, 72, (0, 128, 0))

# Главный игровой цикл
while not done:
    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Закрытие окна
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Выход по клавише Esc
            done = True

    screen.fill((255, 255, 255))  # Очищаем экран белым цветом
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))  # Отображаем текст по центру

    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # Ограничиваем FPS до 60

pygame.quit()  # Завершаем работу PyGame
