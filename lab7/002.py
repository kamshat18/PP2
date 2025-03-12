import os
import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")
base_path = "lab7"
songs = [os.path.join(base_path, "song01.mp3"),
         os.path.join(base_path, "song02.mp3"),
         os.path.join(base_path, "song03.mp3")]
current_song = 0  
player_image = pygame.image.load("music_player.jpg") 
player_image = pygame.transform.scale(player_image, (500, 500)) 
pygame.mixer.music.load(songs[current_song])
running = True
while running:
    screen.fill((30, 30, 30)) 
    screen.blit(player_image, (0, 0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                print("▶ Playing:", songs[current_song])

            elif event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("⏸ Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("▶ Resumed")

            elif event.key == pygame.K_RIGHT:  
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                print("⏭ Next:", songs[current_song])

            elif event.key == pygame.K_LEFT:  
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                print("⏮ Previous:", songs[current_song])

    pygame.display.flip() 

pygame.quit()  
