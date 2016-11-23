import random
import pygame

class asteroidleft:
    
    def __init__(self):
        self.rand_x = random.randint(-90, -30)
        self.rand_y = random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
    def move(self):
        if self.rand_x < 0:
            self.rand_x_change += random.randint(10,20)
        if self.rand_x > 1350:
            self.rand_x_change += -random.randint(10,20)
        self.rand_x += self.rand_x_change
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])
        
class asteroidright:
    
    def __init__(self):
        self.rand_x = random.randint(1351, 1400)
        self.rand_y = random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
    def move(self):
        random_change = random.randint(10,100)
        if self.rand_x < -90:
            self.rand_x_change += 10
        if self.rand_x > 1350:
            self.rand_x_change += -10
        self.rand_x += self.rand_x_change
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])

class asteroidup:
    
    def __init__(self):
        self.rand_x = random.randint(0, 1240)
        self.rand_y = random.randint(-90,-30)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
        self.rand_y_change = 0
    def move(self):
        if self.rand_y < -20:
            self.rand_y_change += 10
        if self.rand_y > 800:
            self.rand_y_change += -10
        self.rand_y += self.rand_y_change
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])


pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
fps = 30

BLACK = 0,0,0
GREY = 126,126,126
RED = 255,0,0
objectsleft = []
for o in range(5):
    asteroid1 = asteroidleft()
    objectsleft.append(asteroid1)

objectsright = []
for a in range(5):
    asteroid2 = asteroidright()
    objectsright.append(asteroid2)

objectsup = []
for b in range(5):
    asteroid3 = asteroidup()
    objectsup.append(asteroid3)

def gameLoop():
    gameOver = False
    me_x = (width-25)/2
    me_y = (height-25)/2
    
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                gameOver = True

        screen.fill(BLACK)
        for asteroid1 in objectsleft:
            asteroid1.draw()
        for asteroid2 in objectsright:
            asteroid2.draw()
        for asteroid3 in objectsup:
            asteroid3.draw()
        for asteroid1 in objectsleft:
            asteroid1.move()
        for asteroid2 in objectsright:
            asteroid2.move()
        for asteroid3 in objectsup:
            asteroid3.move()
        pygame.draw.rect(screen, RED, [me_x,me_y,50,50])
        pygame.display.flip()
        clock.tick(fps)

gameLoop()
pygame.quit()
        
