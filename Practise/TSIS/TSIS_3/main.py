import pygame, sys
from better_race import *
from ui import *
from persistence import *

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

bg = pygame.image.load("Practise/PyGame/Practise 8/Race/Images/road.jpg")
state = "MENU"
score = 0
speed = 5

scores_file = "leaderboard.json"
top_scores = load_data(scores_file, [])

def reset():
    global score, speed, p, enemies, coins, bonuses, all_sprites
    score = 0
    speed = 5
    p = Player()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(p)

reset()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))

    if state == "MENU":
        draw_text(screen, "RACER GAME", 50, W//2, 200)
        if draw_btn(screen, "START", W//2, 400, 200, 50):
            reset()
            state = "GAME"
        if draw_btn(screen, "SCORES", W//2, 500, 200, 50):
            state = "SCORES"

    elif state == "SCORES":
        draw_text(screen, "TOP 10", 40, W//2, 100)
        for i, s in enumerate(top_scores[:10]):
            draw_text(screen, f"{i+1}. {s}", 30, W//2, 150 + i*40)
        if draw_btn(screen, "BACK", W//2, 700, 200, 50):
            state = "MENU"

    elif state == "GAME":
        p.move()
        if len(enemies) < 2:
            e = Enemy(speed)
            enemies.add(e)
            all_sprites.add(e)
        if len(coins) < 1:
            c = Coin(speed)
            coins.add(c)
            all_sprites.add(c)
        if len(bonuses) < 1 and random.randint(1, 500) == 1:
            b = Bonus(speed)
            bonuses.add(b)
            all_sprites.add(b)

        for s in all_sprites:
            if s != p: s.move()
            screen.blit(s.image, s.rect)
        
        if pygame.sprite.spritecollideany(p, enemies):
            if p.shield:
                p.shield = False
                for e in pygame.sprite.spritecollide(p, enemies, True): pass
            else:
                top_scores.append(score)
                top_scores.sort(reverse=True)
                save_data(scores_file, top_scores)
                state = "OVER"

        for c in pygame.sprite.spritecollide(p, coins, True):
            score += 1
            if score % 5 == 0: speed += 1

        for b in pygame.sprite.spritecollide(p, bonuses, True):
            if b.type == "shield": p.shield = True
            if b.type == "nitro": p.nitro = 180

        draw_text(screen, f"Score: {score}", 30, 70, 30)

    elif state == "OVER":
        draw_text(screen, "GAME OVER", 50, W//2, 300)
        draw_text(screen, f"Final Score: {score}", 30, W//2, 400)
        if draw_btn(screen, "MENU", W//2, 550, 200, 50):
            state = "MENU"

    pygame.display.update()
    clock.tick(60)