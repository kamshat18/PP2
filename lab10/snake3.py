# snake.py
import pygame
import sys
from db import get_or_create_user, get_user_score, save_user_progress

pygame.init()

username = input("Введите ваше имя: ")
user_id = get_or_create_user(username)
level, saved_score = get_user_score(user_id)

print(f"Привет, {username}! Уровень: {level}, очки: {saved_score}")

#  Настройки экрана и игры
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
speed = 10 + level * 2

score = saved_score
snake_pos = [100, 50]
snake_body = [[100, 50]]
direction = 'RIGHT'

running = True
paused = False

def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

while running:
    win.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Пауза и сохранение
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print(" Пауза")
                    save_user_progress(user_id, level, score)
                else:
                    print(" Продолжение")

    if not paused:
        snake_pos[0] += 10 if direction == 'RIGHT' else -10 if direction == 'LEFT' else 0
        snake_pos[1] += 10 if direction == 'DOWN' else -10 if direction == 'UP' else 0
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()
        score += 1

    draw_snake()
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
save_user_progress(user_id, level, score)
print(" Qame over. Progress is saved")
