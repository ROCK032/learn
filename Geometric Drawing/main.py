import pygame

# Инициализация PyGame
pygame.init()

# Создание окна 1280x720
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Переключение объектов")

# Определяем цвета
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 128, 0)
white = (255, 255, 255)

# Шрифт для текста
font = pygame.font.Font(None, 50)

# Переменные для движения объектов
circle_y = 170
rect_x = 100
triangle_y = 400

circle_speed = 2
rect_speed = 2
triangle_speed = 2

# Переменная для отслеживания текущего объекта (0 - круг, 1 - прямоугольник, 2 - треугольник)
active_object = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажатие пробела переключает активный объект
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            active_object += 1  # Переключаем на следующий объект
            if active_object > 2:  # Если больше 2, возвращаем на 0
                active_object = 0

    # Очищаем экран
    screen.fill(black)

    # Рисуем только один объект, в зависимости от active_object
    if active_object == 0:  # Двигается круг
        circle_y += circle_speed
        if circle_y >= 650 or circle_y <= 50:
            circle_speed = -circle_speed
        pygame.draw.circle(screen, red, (400, int(circle_y)), 70)

    elif active_object == 1:  # Двигается прямоугольник
        rect_x += rect_speed
        if rect_x >= 1080 or rect_x <= 100:
            rect_speed = -rect_speed
        pygame.draw.rect(screen, blue, pygame.Rect(rect_x, 100, 100, 100))

    elif active_object == 2:  # Двигается треугольник
        triangle_y += triangle_speed
        if triangle_y >= 500 or triangle_y <= 300:
            triangle_speed = -triangle_speed
        pygame.draw.polygon(screen, green, [(300, int(triangle_y)), (400, 300), (400, int(triangle_y) + 50)])

    # Выводим текст с текущим активным объектом
    if active_object == 0:
        text = font.render("Круг", True, white)
    elif active_object == 1:
        text = font.render("Прямоугольник", True, white)
    else:
        text = font.render("Треугольник", True, white)

    text_rect = text.get_rect(center=(640, 50))
    screen.blit(text, text_rect)

    # Обновляем экран
    pygame.display.flip()

pygame.quit()
