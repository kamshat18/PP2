import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#Screen info
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размеры окон, скорость и сколько очков
SCREEN_WIDTH = 400 #Размер окна
SCREEN_HEIGHT = 600
SPEED = 5#Скорость игрока
SCORE = 0#очки за монеты
MONEY_SPEED = 5#скорость монетки
COLLECTED_COINS = 0

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#создание обьектов для игры
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.value = random.randint(1, 3)  # рандом значение монетки

    def move(self):
        self.rect.y += MONEY_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.value = random.randint(1, 3)  # новое значение после возрождение

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# ускорение
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # увелечение скорости врага каждую секунду
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    DISPLAYSURF.blit(background, (0, 0))

    # проверка коллизию между  игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # проверка коллизию между  игроком и мрнетками
    if pygame.sprite.spritecollideany(P1, coins):
        coin = pygame.sprite.spritecollideany(P1, coins)  
        SCORE += coin.value  # добавить валуе в скор
        COLLECTED_COINS += 1
        coin.reset_position()  #обновить позицию ммонеты

        if COLLECTED_COINS % 3 == 0:  # за каждые 3 монетки увеличивать скорость врага
            SPEED += 1


    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    level_text = font_small.render(f"Level: {COLLECTED_COINS // 3}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH - 100, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
""" 1. Racer
Extend example project from Lab 8 and add following tasks: Extra tasks to the given tutorial:

Randomly generating coins with different weights on the road
Increase the speed of Enemy when the player earns N coins
Comment your code """