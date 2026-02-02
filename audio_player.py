import pygame
import time


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play(self, file_path):
        try:
            print("▶ Playing audio...")
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

            # Wait until finished
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            pygame.mixer.music.stop()

        except Exception as e:
            print("Audio error:", e)
