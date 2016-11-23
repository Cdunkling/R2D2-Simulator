import sys
import pygame

pygame.init()
display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

robotImg = pygame.image.load('Robot.png')
backgroundImg = pygame.image.load('Background.png')


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Our Simulator')
clock = pygame.time.Clock()




def robot(x,y):
    gameDisplay.blit(robotImg,(x,y))
def background():
    gameDisplay.blit(background, (0,0))
def rects ():
    rectone = pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
def sim_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    
    x_change = 0
    y_change = 0

    Lbuffer = 20
    Rbuffer = 800-45
    Tbuffer = 20
    Bbuffer = 600-45
    boxx  = 45
    boxxx = 65
    boxy  = 45
    boxyy = 65
    


    gameExit = 0

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                elif event.key == pygame.K_LEFT:
                    x_change = -2
                elif event.key == pygame.K_RIGHT:
                    x_change = 2
                elif event.key == pygame.K_UP:
                    y_change = -2
                elif event.key == pygame.K_DOWN:
                    y_change = 2
                    
            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     x_change = 0
                 elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                     y_change = 0  

        
        x += x_change
        y += y_change
        if x > Rbuffer:
            x = Rbuffer
        if x < Lbuffer:
            x = Lbuffer
        if y > Bbuffer:
            y = Bbuffer
        if y < Tbuffer:
            y = Tbuffer
        if x > boxx and x < boxxx and y > boxy and y < boxyy:
            x = boxx + 20
            y = boxy + 20
        



        
        gameDisplay.blit(backgroundImg, (0,0))       
        robot(x,y)        
        pygame.display.update()
        
        clock.tick(144)

sim_loop()
pygame.quit()
quit()
