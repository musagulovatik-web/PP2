import pygame, random
from pygame.locals import *

W, H = 480, 900

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Practise/PyGame/Practise 8/Race/Images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (W // 2, H - 100)
        self.base_speed = 5
        self.shield = False
        self.nitro = 0

    def move(self):
        k = pygame.key.get_pressed()
        speed = self.base_speed
        if self.nitro > 0:
            speed = 10
            self.nitro -= 1
        
        if k[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-speed, 0)
        if k[K_RIGHT] and self.rect.right < W:
            self.rect.move_ip(speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, s):
        super().__init__()
        self.image = pygame.image.load("Practise/PyGame/Practise 8/Race/Images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), -100)
        self.speed = s

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > H:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, s):
        super().__init__()
        self.image = pygame.image.load("Practise/PyGame/Practise 8/Race/Images/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), -100)
        self.speed = s

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > H:
            self.kill()

class Bonus(pygame.sprite.Sprite):
    def __init__(self, s):
        super().__init__()
        self.type = random.choice(["shield", "nitro"])
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0) if self.type == "shield" else (255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), -100)
        self.speed = s

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > H:
            self.kill()