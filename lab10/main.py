import pygame
import sys
from db import get_or_create_user, get_user_score, save_user_progress

# Game setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# Game variables
current_level = 1
current_score = 0
game_running = True
paused = False

# Snake game logic here...

# Function to show the main menu and get username
def get_username():
    username = input("Enter your username: ")
    user_id = get_or_create_user(username)
    user_score = get_user_score(user_id)
    
    if user_score:
        print(f"Welcome back {username}! Your current level is {user_score[0]} and score is {user_score[1]}")
    else:
        print(f"Welcome {username}! This is your first time playing.")

    return user_id

# Pause and save game progress
def pause_game(user_id):
    global paused
    paused = not paused
    if paused:
        print("Game paused. Press 'P' to resume.")
    else:
        save_user_progress(user_id, current_level, current_score)
        print(f"Game saved. Current level: {current_level}, score: {current_score}")

# Main game loop
def game_loop():
    global current_level, current_score, game_running
    
    user_id = get_username()
    
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press P to pause
                    pause_game(user_id)
                # Add other key events for snake control here

        if not paused:
            # Update the game state (move snake, check collisions, etc.)
            # You would implement the logic of the snake game here,
            # updating `current_level` and `current_score` as the game progresses.
            pass
        
        # Refresh the screen
        screen.fill((0, 0, 0))  # Black background
        pygame.display.flip()
        
        clock.tick(15)  # Frame rate (adjust for difficulty)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
