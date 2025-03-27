import pygame
import random
import sys
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
SPEED = 7 

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Verdana", 20)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # начальное тело
        self.direction = (CELL_SIZE, 0)  # направление вправо
        self.grow = False 

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if not self.grow:
            self.body.pop()  # удаляем хвост
        self.body.insert(0, new_head)  # добавляем голову
        self.grow = False

    def change_direction(self, direction):
        # Запрещаем поворот в обратную сторону
        if (direction[0] != -self.direction[0] and direction[1] != -self.direction[1]):
            self.direction = direction

    def check_collision(self):
        head = self.body[0]
        # Столкновение с телом или выход за границу
        if head in self.body[1:] or head[0] < 0 or head[1] < 0 or head[0] >= SCREEN_WIDTH or head[1] >= SCREEN_HEIGHT:
            return True
        return False

    def grow_snake(self):
        self.grow = True  
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def respawn(self, snake_body):
        self.position = self.generate_position(snake_body)

snake = Snake()
food = Food(snake.body)

score = 0
level = 1

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))

    snake.move()

    if snake.check_collision():
        running = False

    # Проверка, съела ли змея еду
    if snake.body[0] == food.position:
        score += 1
        snake.grow_snake()
        food.respawn(snake.body)

        # Повышаем уровень и скорость каждые 3 очка
        if score % 3 == 0:
            level += 1
            SPEED += 2

    
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    
    pygame.draw.rect(screen, RED, pygame.Rect(food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()
sys.exit()
