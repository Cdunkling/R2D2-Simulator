import pygame
import random
from os import path
img_dir = path.join(path.dirname(__file__), 'img') #directory for files

pygame.init()
pygame.mixer.init()
#dimensions and the FPS for the game
WIDTH = 400
HEIGHT = 600
FPS = 60

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#create window

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ASTEROID SMASHER")
clock = pygame.time.Clock()


#creates the player's "ship"
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(ship_img, (50,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0


        
    def update(self):

        self.speedx=0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
#shoots bullets
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)
        
#generating obstacles at random places at random speed (1-8) 
class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(obstacle_img, (40,40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)


    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 3)

#creating bullets 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img #bullet image
        self.image.set_colorkey(BLACK) #removes the background colour of the image
        self.rect = self.image.get_rect() 
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10


    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom <0: 
            self.kill() # if bullet moves off the screen, it gets deleted. 
            
#load all images
background = pygame.image.load(path.join(img_dir, "background.png")).convert()
background_rect = background.get_rect()
ship_img = pygame.image.load(path.join(img_dir, "ship.png")).convert()
obstacle_img = pygame.image.load(path.join(img_dir, "obstacle.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laser.png")).convert()

sprites = pygame.sprite.Group() #a group for all objects
obstacles = pygame.sprite.Group() #a group for obstacles
bullets = pygame.sprite.Group() #a group for bullets
ship = Ship() #player ship
sprites.add(ship)
for i in range(2): #how many obstacles appear on the screen at one time. 
    o = Obstacles()
    sprites.add(o)
    obstacles.add(o)



# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()
                

    # Update
    sprites.update()

#check if an obstacle has hit the ship
    collisions = pygame.sprite.spritecollide(ship, obstacles, False)
    if collisions:
        running = False

    # Draw stuff
    display.fill(BLACK)
    display.blit(background, background_rect)
    sprites.draw(display)
    #updates or flips the display
    pygame.display.flip()

pygame.quit() #quits pygame
