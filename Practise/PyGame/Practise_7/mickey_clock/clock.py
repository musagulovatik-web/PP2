import pygame
import os

class MickeyClock:
    def __init__(self):
        self.W, self.H = 600, 400
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Mickey Clock")
        self.cx, self.cy = self.W // 2, self.H // 2
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 28, bold=True)
        
        base = os.path.dirname(__file__)
        img_path = os.path.join(base, "images")
        self.face = pygame.image.load(os.path.join(img_path, "clock_face.png")).convert_alpha()
        self.face = pygame.transform.scale(self.face, (self.W, self.H))