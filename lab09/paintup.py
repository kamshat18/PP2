import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600  # размер экрана
WHITE = (255, 255, 255)  # белый
BLACK = (0, 0, 0)  # черный
RED = (255, 0, 0)  # красный
GREEN = (0, 255, 0)  # зеленый
BLUE = (0, 0, 255)  # синий
COLORS = [BLACK, RED, GREEN, BLUE, WHITE]  # палитра цветов
COLOR_NAMES = ["Black", "Red", "Green", "Blue", "Eraser"]  # названия цветов
BUTTON_SIZE = 50  # размер кнопок

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем экран
pygame.display.set_caption("Smooth Drawing Tool")  # заголовок окна
screen.fill(WHITE)  # фон белый

# Variables
current_color = BLACK  # начальный цвет
drawing = False  # рисуем ли
mode = "pen"  # начальный режим — ручка
start_pos = None  # начальная позиция
points = []  # точки для рисования

# UI Elements (кнопки для выбора цвета)
buttons = []
for i, color in enumerate(COLORS):
    buttons.append(pygame.Rect(10 + i * (BUTTON_SIZE + 10), HEIGHT - 60, BUTTON_SIZE, BUTTON_SIZE))

# Функция отрисовки кнопок
def draw_ui():
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, COLORS[i], button)  # рисуем кнопки
        if COLORS[i] == WHITE:  # если это ластик, обводим
            pygame.draw.rect(screen, BLACK, button, 2)
        if COLORS[i] == current_color:  # выделяем выбранный цвет
            pygame.draw.rect(screen, WHITE, button, 3)

# Функция получения цвета по позиции
def get_color_from_pos(pos):
    for i, button in enumerate(buttons):
        if button.collidepoint(pos):
            return COLORS[i]  # если кнопка нажата, возвращаем цвет
    return None

# Рисуем плавную линию
def draw_smooth_line(screen, points, width, color):
    if len(points) < 2:  # если точек меньше 2, нечего рисовать
        return
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))
        for j in range(iterations):
            progress = j / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            pygame.draw.circle(screen, color, (x, y), width)  # рисуем плавную линию

# квадрат
def draw_square(start, end, color):
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    pygame.draw.rect(screen, color, (x, y, width, height), 2)  # рисуем квадрат

#прямоугольный треугольник
def draw_right_triangle(start, end, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y1), (x2, y2)], 2)  # рисуем прямоугольный треугольник
#равносторонний треугольник
def draw_equilateral_triangle(start, end, color):
    x1, y1 = start
    x2, y2 = end
    side = max(abs(x2 - x1), abs(y2 - y1))
    height = (3 ** 0.5 / 2) * side  # высота равностороннего треугольника
    x3 = (x1 + x2) / 2
    y3 = y1 - height
    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3)], 2)  # рисуем равносторонний треугольник

# Рисуем ромб
def draw_rhombus(start, end, color):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    pygame.draw.polygon(screen, color, [(x1, y1), (x1 + width, y1 + height), (x2, y2), (x2 - width, y2 - height)], 2)  # рисуем ромб

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # если нажата левая кнопка мыши
                new_color = get_color_from_pos(event.pos)  # получаем цвет по позиции
                if new_color is not None:
                    current_color = new_color  # меняем цвет
                    mode = "eraser" if new_color == WHITE else "pen"  # если выбрали ластик — меняем режим
                else:
                    drawing = True  # начинаем рисовать
                    start_pos = event.pos  # начальная позиция
                    points = [start_pos]  # добавляем точку

        elif event.type == pygame.MOUSEBUTTONUP:
            # Если завершено рисование в выбранном режиме
            if mode == "rectangle" and start_pos:
                end_pos = event.pos
                draw_square(start_pos, end_pos, current_color)
            elif mode == "right_triangle" and start_pos:
                end_pos = event.pos
                draw_right_triangle(start_pos, end_pos, current_color)
            elif mode == "equilateral_triangle" and start_pos:
                end_pos = event.pos
                draw_equilateral_triangle(start_pos, end_pos, current_color)
            elif mode == "rhombus" and start_pos:
                end_pos = event.pos
                draw_rhombus(start_pos, end_pos, current_color)
            drawing = False  # заканчиваем рисовать
            points = []

        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode == "pen":  # если рисуем ручкой
                points.append(event.pos)  # добавляем точку
                draw_smooth_line(screen, points, 5, current_color)  # рисуем плавную линию
                points = points[-2:]  # оставляем только последние 2 точки
            elif drawing and mode == "eraser":  # если рисуем ластиком
                pygame.draw.circle(screen, WHITE, event.pos, 10)  # рисуем круг для стирания

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mode = "pen"  # режим рисования ручкой
            elif event.key == pygame.K_e:
                mode = "eraser"  # режим ластика
            elif event.key == pygame.K_r:
                mode = "rectangle"  # рисуем квадрат
            elif event.key == pygame.K_t:
                mode = "right_triangle"  # рисуем прямоугольный треугольник
            elif event.key == pygame.K_c:
                mode = "equilateral_triangle"  # рисуем равносторонний треугольник
            elif event.key == pygame.K_h:
                mode = "rhombus"  # рисуем ромб

    draw_ui()  # отрисовка интерфейса
    pygame.display.flip()  # обновляем экран
    clock.tick(60)  # частота кадров

pygame.quit()
sys.exit()

""" 
Для рисования:
- квадрат: нажать R
- прямоугольный треугольник: нажать T
- равносторонний треугольник: нажать C
- ромб: нажать H
"""
