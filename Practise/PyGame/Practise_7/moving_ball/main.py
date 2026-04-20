import pygame
import ball
pygame.init()
W=900
H=600
sc=pygame.display.set_mode((W,H))
x=W//2
y=H//2
running=True
while running:
    sc.fill((255,255,255))
    pygame.draw.circle(sc, (255,0,0), (x,y), 25)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            k = 0
            if event.key == pygame.K_UP: 
                k = 1
            if event.key == pygame.K_DOWN:
                k = 2
            if event.key == pygame.K_LEFT:
                k = 3
            if event.key == pygame.K_RIGHT:
                k = 4
            x, y = ball.mb(x, y, k, W, H)

    pygame.display.flip()
    clock=pygame.time.Clock()
    clock.tick(60)

pygame.quit()