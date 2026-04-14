import pygame
pygame.init()
screen=pygame.display.set_mode((600,300))
pygame.display.set_caption("Ateik")
icon=pygame.image.load('Practise\PyGame\Images\kimono.png')
pygame.display.set_icon(icon)
running=True
while running:
    #screen.fill((255,0,255))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                screen.fill((255,255,255))
            if event.key==pygame.K_d:
                screen.fill((0,0,0))