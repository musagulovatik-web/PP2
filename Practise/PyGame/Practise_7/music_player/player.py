import pygame
import os
playlist = [f for f in os.listdir(os.path.join(os.path.dirname(__file__), "music")) if f.endswith(('.wav', '.mp3'))]
c = 0
def play_music():
    if playlist:
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "music", playlist[c]))
        pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()
def next_track():
    global c
    c = (c + 1) % len(playlist)
    play_music()
def prev_track():
    global c
    c = (c - 1) % len(playlist)
    play_music()