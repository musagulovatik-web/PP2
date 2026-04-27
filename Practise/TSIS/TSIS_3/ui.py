import pygame

def draw_text(sc, txt, size, x, y, color=(255, 255, 255)):
    f = pygame.font.SysFont("Arial", size)
    img = f.render(str(txt), True, color)
    rect = img.get_rect(center=(x, y))
    sc.blit(img, rect)

def draw_btn(sc, txt, x, y, w, h):
    r = pygame.Rect(x - w//2, y - h//2, w, h)
    pygame.draw.rect(sc, (50, 50, 50), r)
    draw_text(sc, txt, 30, x, y)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if r.collidepoint(mouse) and click[0]:
        return True
    return False