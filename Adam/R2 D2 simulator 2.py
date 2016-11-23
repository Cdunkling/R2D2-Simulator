import pygame
import sys
import random

pygame.init()
width = 1200
hieght = 800

gameDisplay = pygame.display.set_mode((width, hieght))
pygame.display.set_caption('Simulator')
clock = pygame.time.Clock()

RED = (255,0,0)
GREY = (138,138,138)
BLACK = (0,0,0)

def asteroid(x_start, y_start, ast_size):
    pygame.draw.rect(gameDisplay, GREY, [x_start, y_start, ast_size, ast_size])
def ship():
    False
    
def rect_overlap(a, b):
    return \
    a[0] < b[0] + b[2] and \
    a[0] + a[2] > b[0] and \
    a[1] < b[1] + b[3] and \
    a[1] + a[3] > b[1]
def simulator():
    ast_size = 50
    rob_size = 10
    bul_size = 5
    fps = 60

    gameExit = False
    gameOver = False
    x_change = width/2
    y_change = hieght/2
    x_start = -90
    y_start = random.randrange(50, 700)


    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    gameOver = False
                    gameExit = True

        
        x_start +=10
        y_start += random.randint(1,11)
        gameDisplay.fill(BLACK)
        asteroid(x_start, y_start, ast_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
simulator()
    
