import pygame
import datetime
import math
import sys
from clock import MickeyClock

def get_end(angle_deg, length, cx, cy):
    angle_rad = math.radians(angle_deg - 90)
    x = cx + length * math.cos(angle_rad)
    y = cy + length * math.sin(angle_rad)
    return x, y

def main():
    pygame.init()
    app = MickeyClock()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        now = datetime.datetime.now()
        h = now.hour % 12
        m = now.minute
        s = now.second

        hour_angle = h * 30 + m * 0.5
        minute_angle = m * 6 + s * 0.1
        second_angle = s * 6

        app.screen.fill((255, 255, 255))
        app.screen.blit(app.face, (0, 0))

        hx, hy = get_end(hour_angle, 70, app.cx, app.cy)
        pygame.draw.line(app.screen, (0, 0, 0), (app.cx, app.cy), (hx, hy), 6)

        mx, my = get_end(minute_angle, 100, app.cx, app.cy)
        pygame.draw.line(app.screen, (30, 30, 30), (app.cx, app.cy), (mx, my), 4)

        sx, sy = get_end(second_angle, 120, app.cx, app.cy)
        pygame.draw.line(app.screen, (255, 0, 0), (app.cx, app.cy), (sx, sy), 2)

        pygame.draw.circle(app.screen, (0, 0, 0), (app.cx, app.cy), 6)

        text = app.font.render(now.strftime("%H:%M:%S"), True, (255, 0, 0), (239, 228, 176))
        app.screen.blit(text, (430, 350))

        pygame.display.flip()
        app.clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()