import pygame
import sys
import player
pygame.init()
pygame.mixer.init()
sc=pygame.display.set_mode((900,600))
ft=pygame.font.Font(None, 24)
running=True
ply=False
while running:
    sc.fill((0,0,0))
    if player.playlist:
        track_name = player.playlist[player.current_track_index]
        text_surface = ft.render(f"Now Playing: {track_name}", True, (255,255,255))
        sc.blit(text_surface, (50, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play_music()
                is_playing = True
            elif event.key == pygame.K_s:
                player.stop_music()
                is_playing = False
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q: 
                running = False
        pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()