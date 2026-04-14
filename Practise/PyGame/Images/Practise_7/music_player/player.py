import pygame
import os
playlist = [f for f in os.listdir(os.path.join(os.path.dirname(__file__), "music")) if f.endswith(('.wav', '.mp3'))]
current_track_index = 0
def play_music():
    if playlist:
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "music", playlist[current_track_index]))
        pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()
def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(playlist)
    play_music()
def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(playlist)
    play_music()