import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Настройки экрана и шрифтов
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Improved Game")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифты
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Фон и звук
background = pygame.image.load("AnimatedStreet.png")
crash_sound = pygame.mixer.Sound("crash.wav")

# Игровые переменные
FPS = 60
FramePerSec = pygame.time.Clock()
SPEED = 5
SCORE = 0
LIVES = 3
game_active = True

# Игрок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Враг
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Функция для сброса игры
def reset_game():
    global SCORE, LIVES, SPEED, game_active
    SCORE = 0
    LIVES = 3
    SPEED = 5
    game_active = True
    for enemy in enemies:
        enemy.rect.top = 0
        enemy.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    player.rect.center = (160, 520)

# Создание объектов
player = Player()
enemies = pygame.sprite.Group()
for _ in range(3):  # 3 врага
    enemies.add(Enemy())

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)

# Таймер ускорения
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED and game_active:
            SPEED += 0.5
        if not game_active and event.type == KEYDOWN and event.key == K_r:
            reset_game()

    DISPLAYSURF.blit(background, (0, 0))

    if game_active:
        # Движение объектов
        player.move()
        for enemy in enemies:
            enemy.move()

        # Отрисовка
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)

        # Отображение счёта и жизней
        score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
        lives_text = font_small.render(f"Lives: {LIVES}", True, BLACK)
        DISPLAYSURF.blit(score_text, (10, 10))
        DISPLAYSURF.blit(lives_text, (300, 10))

        # Столкновение
        if pygame.sprite.spritecollideany(player, enemies):
            crash_sound.play()
            LIVES -= 1
            time.sleep(0.5)
            if LIVES <= 0:
                game_active = False
    else:
        # Экран Game Over
        DISPLAYSURF.fill(RED)
        game_over_text = font_big.render("Game Over", True, BLACK)
        restart_text = font_small.render("Press R to restart", True, BLACK)
        DISPLAYSURF.blit(game_over_text, (50, 200))
        DISPLAYSURF.blit(restart_text, (120, 300))

    pygame.display.update()
    FramePerSec.tick(FPS)
