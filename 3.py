import pygame
import sys
 
FPS = 60
W, H = 500, 400  
 
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 

x = W // 2
y = H // 2
r = 25
 
while 1:
    if x < 25:
        x+=20
    if y < 25:
        y+=20
    if x > W-25:
        x-=20
    if y > H-25:
        y-=20

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 20
            elif i.key == pygame.K_RIGHT:
                x += 20
            elif i.key == pygame.K_UP:
                y -= 20
            elif i.key == pygame.K_DOWN:
                y += 20
 
    sc.fill('white')
    pygame.draw.circle(sc, 'red', (x, y), r)
    pygame.display.update()
    clock.tick(FPS)
