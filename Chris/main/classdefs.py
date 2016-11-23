
import pygame,pygame.locals,random,os,math
from main import stats
pygame.font.init()
class killerrobot(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.orgimage = pygame.image.load('player_sprite.png')
        self.image=pygame.image.load('player_sprite.png')
        self.rect = self.image.get_rect()
        self.rect.left = 550
        self.rect.top = 400
        self.exp =0
        self.weapon="pistol"
        self.speed=4
        self.angle = 0
        self.health=50

    def rotate(self,mousepos):
        self.angle = math.degrees(math.atan2(self.rect.centerx - mousepos[0], self.rect.centery - mousepos[1]))

        self.image = pygame.transform.rotate(self.orgimage, self.angle)

        self.rect = self.image.get_rect(center=self.rect.center)
    def takedamage(self,damage,screen):
        self.health-=round(damage-stats.RobotStats['Armour']/10)
        if self.health>0:
            return True
        else:
            return False
    def getangle(self):
        return self.angle

    def getpos(self):
        return [self.rect.centerx,self.rect.centery]


    def go_left(self, screen):
        if self.rect.left < 0:
            None
        else:
            self.rect.left -= self.speed

    def go_right(self, screen):
        if self.rect.right > 1024:
            None
        else:
            self.rect.right += self.speed

    def go_up(self, screen):
        if self.rect.top < 50:
            None
        else:
            self.rect.top -= self.speed

    def go_down(self, screen):
        if self.rect.bottom > screen.get_height():
            None
        else:
            self.rect.bottom += self.speed
    def giveexp(self,exp):
        self.exp+=exp


class Text(pygame.sprite.Sprite):
    def __init__(self, size, color, position,variable,message, alpha):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("./AmazDooMRight2.ttf", size)
        self.color = color
        self.position = position
        self.variable=variable

        self.message = message
        self.m = ''
        self.alpha = alpha

    def set_variable(self,variable):
        if variable:
            self.variable=variable
    def setalpha(self,alpha):
            self.alpha=alpha

    def update(self):
        if self.variable!=None:
            self.m = self.message+self.variable
        else:
            self.m=self.message
        self.image = self.font.render(self.m, 1, self.color)
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect()
        self.rect.center = (self.position)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, image,angle,player_pos,mouse_pos,speed,damage):
        pygame.sprite.Sprite.__init__(self)
        self.x = player_pos[0]
        self.y = player_pos[1]
        self.damage=damage

        # Assign the mouse target position
        self.targetx = mouse_pos[0]
        self.targety = mouse_pos[1]

        if image:
            self.image=image
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)
            self.image=pygame.transform.rotate\
            (self.image, angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image=pygame.Surface((5,5))
            self.image.fill((255,0,0))
            self.image.set_alpha(0)
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)

        self.distance = math.sqrt \
            (pow(self.targetx - self.x, 2) + pow(self.targety - self.y, 2))
        self.animation_steps = self.distance / speed
        self.dx = (self.targetx - self.x) / self.animation_steps
        self.dy = (self.targety - self.y) / self.animation_steps

    def getdamage(self):
        return self.damage

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top < 0 or self.rect.bottom > 1024 or self.rect.left < 0 or self.rect.right > 1024:
            self.kill()
class enemyBullet(pygame.sprite.Sprite):

    def __init__(self, image,angle,player_pos,speed,damage):
        pygame.sprite.Sprite.__init__(self)
        self.x = player_pos[0]
        self.y = player_pos[1]
        self.damage=damage

        self.targetx = 550
        self.targety = 450

        if image:
            self.image=image
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)
            self.image=pygame.transform.rotate\
            (self.image, angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image=pygame.Surface((5,5))
            self.image.fill((255,0,0))
            self.image.set_alpha(0)
            self.rect = self.image.get_rect()
            self.rect.center=(self.x,self.y)

        self.__distance = math.sqrt \
            (pow(self.targetx - self.x, 2) + pow(self.targety - self.y, 2))
        self.animation_steps = self.__distance / speed
        self.dx = (self.targetx - self.x) / self.animation_steps
        self.dy = (self.targety - self.y) / self.animation_steps

    def getdamage(self):
        return self.damage

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top < 0 or self.rect.bottom > 1024 or self.rect.left < 0 or self.rect.right > 1024:
            self.kill()

class enemy(pygame.sprite.Sprite):

    def __init__(self, image, playerpos, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image.convert_alpha()
        self.org=self.image
        self.screen = screen
        self.rect = self.image.get_rect()
        self.speed=10
        self.health=10
        self.spawn()
        self.givenxp=1
        self.rotate(playerpos)
        self.set_step_amount(playerpos)

    def spawn(self):
        spawnchoice=random.randint(1,4)
        if spawnchoice==1:
            self.x = random.randrange(0, -300, -30)
            self.y = random.randint(0, self.screen.get_height() - 100)

        elif spawnchoice==2:
            self.x = random.randrange(0, 1024, 20)
            self.y = random.randint(0, self.screen.get_height() - 100)

        elif spawnchoice==3:
            self.x = random.randrange(0, -300, -30)
            self.y = random.randint(self.screen.get_height(), self.screen.get_height() + 100)

        elif spawnchoice==4:
            self.x = random.randrange(0, 1024, 20)
            self.y = random.randint(self.screen.get_height(), self.screen.get_height() + 100)
        self.rect.center = (self.x, self.y)

    def set_step_amount(self, player_pos):
        try:
            self.distance = math.sqrt \
                (pow(player_pos[0] - self.rect.centerx, 2) + pow(player_pos[1] - self.rect.centery, 2))
            self.animation_steps = self.distance / self.speed
            self.dx = (player_pos[0] - self.rect.centerx) / self.animation_steps
            self.dy = (player_pos[1] - self.rect.centery) / self.animation_steps
        except:
            self.dx = 0
            self.dy = 0

    def rotate(self,playerpos):
        self.angle = math.degrees(math.atan2 \
                                        (self.rect.centerx - playerpos[0], self.rect.centery - playerpos[1]))

        self.image = pygame.transform.rotate \
            (self.org, self.angle)

        self.rect = self.image.get_rect(center=self.rect.center)
    def getangle(self):
        return self.angle

    def damage(self,damagedone):
        self.health-=damagedone
        if self.health>0:
            return True
        else:
            return False

    def update(self):
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
class pistolenemy(enemy):
    def __init__(self, image,playerpos,screen):
        super().__init__(image,playerpos,screen)
        self.givenxp=2
        self.speed=2
        self.health=20
        self.fired=0

    def getfired(self):
            return self.fired

    def setfired(self, time):
            self.fired = time
class boss(enemy):
    def __init__(self, image,playerpos,screen):
        super().__init__(image,playerpos,screen)
        self.speed=0.5
        self.health=500
        self.fired=0
        self.firedr=0
        self.spawn()

    def spawn(self):
        self.rect.center = (500, 900)


    def getfired(self):
            return self.fired

    def setfired(self, time):
            self.fired = time

    def getfiredr(self):
        return self.fired

    def setfiredr(self, time):
        self.firedr = time


class rocketenemy(enemy):
    def __init__(self, image,playerpos,screen):
        super().__init__(image, playerpos, screen)
        self.speed=2
        self.health=50
        self.fired=0
        self.givenxp=10

    def getfired(self):
            return self.fired

    def setfired(self, time):
            self.fired = time

class shotgunpickup(pygame.sprite.Sprite):
    def __init__(self, image,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.convert_alpha()
        self.org = self.image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.spawn()

    def spawn(self):
        self.rect.center = (300,200)

class Rocket(Bullet,pygame.sprite.Sprite):
    def donothing(self):
        x=0
class enemyRocket(enemyBullet,pygame.sprite.Sprite):
    def donothing(self):
        x=0


def text_objects(text, font):
    textSurface = font.render(text, True, [255,255,255])
    return textSurface, textSurface.get_rect()

def message_display(text,screen):
    largeText = pygame.font.Font('AmazDooMRight2.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1024/2),(768/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    pygame.time.sleep(2)

class button(pygame.sprite.Sprite):
    def __init__(self,msg,x,y,w,h,ic,ac,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen,ac,(x,y,w,h))
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("AmazDooMRight2.ttf",20)
        textSurf,textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)
