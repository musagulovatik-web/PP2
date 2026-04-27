import pygame
import sys
import datetime
import sys

pygame.init()

W, H = 1200, 924
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simple Paint - Extended")

canvas = pygame.Surface((W, H))
canvas.fill((255, 255, 255))

mode = 'brush'
color = (0, 0, 0)
thickness = 2  
start_pos = None
drawing = False
prev_pos = None 
text_mode = False
current_text = ""
text_pos = (0, 0)
font = pygame.font.SysFont("Arial", 24)

def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()
    target_color = surface.get_at((x, y))
    
    if target_color == new_color:
        return

    queue = [(x, y)]
    
    while queue:
        cx, cy = queue.pop(0)
        if surface.get_at((cx, cy)) == target_color:
            surface.set_at((cx, cy), new_color)
            if cx + 1 < width: queue.append((cx + 1, cy))
            if cx - 1 >= 0:    queue.append((cx - 1, cy))
            if cy + 1 < height: queue.append((cx, cy + 1))
            if cy - 1 >= 0:    queue.append((cx, cy - 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if text_mode:
                if event.key == pygame.K_BACKSPACE:
                    current_text = current_text[:-1]
                elif event.key == pygame.K_RETURN:
                    text_surface = font.render(current_text, True, color)
                    canvas.blit(text_surface, text_pos)
                    current_text = ""
                    text_mode = False
                elif event.key == pygame.K_ESCAPE:
                    current_text = ""
                    text_mode = False
                else:
                    if event.unicode.isprintable():
                        current_text += event.unicode
            else:
                if event.key == pygame.K_z: color = (255, 0, 0) 
            if event.key == pygame.K_x: color = (0, 0, 255) 
            if event.key == pygame.K_c: color = (0, 0, 0)
            if event.key == pygame.K_q: mode = 'rect'
            if event.key == pygame.K_w: mode = 'circle'
            if event.key == pygame.K_r: mode = 'pencil'
            if event.key == pygame.K_t: mode = 'line'
            if event.key == pygame.K_e: mode = 'eraser'
            if event.key == pygame.K_y: mode = 'fill'
            if event.key == pygame.K_u: mode = 'text'

            if event.key == pygame.K_1: thickness = 2
            if event.key == pygame.K_2: thickness = 5
            if event.key == pygame.K_3: thickness = 10
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                filename = f"painting_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                pygame.image.save(canvas, filename)


        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            prev_pos = event.pos
            if mode == 'text':
                text_pos = event.pos
                text_mode = True
                current_text = ""
            if mode == 'fill':
                flood_fill(canvas, start_pos[0], start_pos[1], color)
            else:
                drawing=True
        
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == 'rect':
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), 
                                abs(start_pos[0]-end_pos[0]), abs(start_pos[1]-end_pos[1]))
                pygame.draw.rect(canvas, color, rect, thickness)
            elif mode == 'circle':
                radius = int(((start_pos[0]-end_pos[0])**2 + (start_pos[1]-end_pos[1])**2)**0.5)
                pygame.draw.circle(canvas, color, start_pos, radius, thickness)
            elif mode == 'line':
                pygame.draw.line(canvas, color, start_pos, end_pos, thickness)
            
            drawing = False
        
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if mode == 'pencil':
            pygame.draw.line(canvas, color, prev_pos, mouse_pos, thickness)
            prev_pos = mouse_pos
        elif mode == 'eraser':
            pygame.draw.circle(canvas, (255, 255, 255), mouse_pos, thickness + 5)

    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))
    
    font = pygame.font.SysFont("Arial", 18)
    text = font.render(f"Mode: {mode} | Size: {thickness} | Color: {color}", True, (0, 0, 0))
    screen.blit(text, (10, 850))
    
    if text_mode:
        text_surface = font.render(current_text, True, color)
        screen.blit(text_surface, text_pos)
    
    pygame.display.update()