import pygame
clock=pygame.time.Clock()
pygame.init()
sc=pygame.display.set_mode((639,360))
running=True
bg=pygame.image.load(r'Practise\PyGame\Images\bon2.jpg')
walk_right=[
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_10.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_11.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_12.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_13.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_14.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_15.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_16.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_17.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_right\skeleton_18.png')
]
walk_left=[
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_1.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_2.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_3.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_4.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_5.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_6.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_7.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_8.png'),
    pygame.image.load('Practise\pyGame\Images\skeleton_left\skeleton_9.png')
]
gg_anim_count=0
bgx=0
bg_sound=pygame.mixer.Sound(r'Practise\PyGame\sound\bg_sound.mp3')
bg_sound.play()
while running:
    clock.tick(60)
    sc.blit(bg, (0,0))
    sc.blit(bg, (bgx+639,0))
    sc.blit(walk_right[gg_anim_count], (200, 270))
    if gg_anim_count==8:
        gg_anim_count=0
    else:
        gg_anim_count+=1
    bgx=bgx-2
    if bgx==-638:
        bgx=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False