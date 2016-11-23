<<<<<<< HEAD
import random

import pygame

pygame.init()


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (900, 700)
done = False

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)##, pygame.FULLSCREEN)
pygame.display.set_caption("Rectangle Bounce Simulator 2K16")
rect_x=random.randrange(50, 850, 1)
rect_y = random.randrange(50, 650, 1)
xdir = random.choice([3,-3])
ydir = xdir
while not done:
    # --- Main event loop
    if rect_y > 650 or rect_y < 0:
        ydir *= -1
    if rect_x > 850 or rect_x < 0:
        xdir *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            done = True
    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[rect_x,rect_y,50,50],0)
    rect_x += xdir
    rect_y += ydir
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
=======
import random

import pygame

pygame.init()


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (900, 700)
done = False

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)##, pygame.FULLSCREEN)
pygame.display.set_caption("Rectangle Bounce Simulator 2K16")
rect_x=random.randrange(50, 850, 1)
rect_y = random.randrange(50, 650, 1)
xdir = random.choice([3,-3])
ydir = xdir
while not done:
    # --- Main event loop
    if rect_y > 650 or rect_y < 0:
        ydir *= -1
    if rect_x > 850 or rect_x < 0:
        xdir *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            done = True
    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[rect_x,rect_y,50,50],0)
    rect_x += xdir
    rect_y += ydir
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
>>>>>>> origin/master
