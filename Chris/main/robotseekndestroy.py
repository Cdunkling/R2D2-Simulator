import pygame,pygame.locals,math,sys

from main import classdefs
from main.stats import RobotStats, Statcalc

"""music and sound setup"""
pygame.mixer.init()
pygame.mixer.music.load("./Contra Hard Corps Music.mp3")
pygame.font.init()
pygame.mixer.music.play(-1)
fire = pygame.mixer.Sound("./DSPISTOL.wav")
fireshotgun = pygame.mixer.Sound("./DSSHOTGN.wav")
firerocket = pygame.mixer.Sound("./DSRLAUNC.wav")
fireplasma = pygame.mixer.Sound("./DSPLASMA.wav")
explode= pygame.mixer.Sound("./DSBAREXP.wav")
pain= pygame.mixer.Sound("./DSPLPAIN.wav")
playerdeath=pygame.mixer.Sound("./DSPLDETH.wav")
"""window+color setup"""
pygame.display.set_caption("Robot simulator 2016")
clock = pygame.time.Clock()
screen=pygame.display.set_mode((1500,768))
rect=screen.get_rect()
white=[255,255,255]
black=[0,0,0]
green=[0,255,0]
red=[255,0,0]
blue=[0,0,255]
"""create the sprite groups"""
bullet_hitbox = pygame.sprite.Group()
bullet_img = pygame.sprite.Group()
ebullet_hitbox = pygame.sprite.Group()
ebullet_img = pygame.sprite.Group()
rocket_hitbox = pygame.sprite.Group()
rocket_img = pygame.sprite.Group()
erocket_hitbox = pygame.sprite.Group()
erocket_img = pygame.sprite.Group()
powerups = pygame.sprite.Group()
enemies = pygame.sprite.Group()
robot_group = pygame.sprite.Group()
smartenemies = pygame.sprite.Group()
explosions = pygame.sprite.Group()
enemy_hitbox = pygame.sprite.Group()
warnings = pygame.sprite.Group()
pistolenemies=pygame.sprite.Group()
rocketenemies=pygame.sprite.Group()
statlist=pygame.sprite.Group()
bosses=pygame.sprite.Group()
weapons=('pistol','shotgun','machine gun','Rocket Launcher','Plasma Rifle','Battle Lord')
"""background"""
spritebg = pygame.Surface(screen.get_size())
spritebg = spritebg.convert()
spritebg.fill((0, 0, 250))
global x
global score
"""resets all variable for running first time and after game over"""
def reset():
    global rapidfire
    global spawnlist
    global rapidfire2
    global rapidfire3
    global rapidfire4
    global rapidfire5
    global lastfired
    global gotshotgun
    global gotmachinegun
    global gotplasmarifle
    global gotrocketlauncher
    global running
    global machinegundelay
    global plasmarifledelay
    global bldelay1
    global bldelay2
    global bldelay3
    global weaponselected
    global allSprites
    global x
    global i
    global score
    global robot
    global shotgun
    global wave_text
    global wave
    global lines
    lines=0
    wave=1
    i=0
    rapidfire=False
    rapidfire2=False
    rapidfire3 = False
    rapidfire4 = False
    rapidfire5 = False
    lastfired=0;
    gotshotgun=False
    gotmachinegun=False
    gotplasmarifle=False
    gotrocketlauncher=False
    running=True
    machinegundelay=0
    plasmarifledelay=0
    bldelay1=0
    bldelay2=0
    bldelay3=0
    weaponselected=1
    bullet_hitbox.empty()
    bullet_img.empty()
    rocket_hitbox.empty()
    rocket_img.empty()
    erocket_hitbox.empty()
    erocket_img.empty()
    powerups.empty()
    enemies.empty()
    robot_group.empty()
    explosions.empty()
    enemy_hitbox.empty()
    warnings.empty()
    pistolenemies.empty()
    rocketenemies.empty()
    bosses.empty()
    x=1
    score=0
    robot = classdefs.killerrobot('./temp_sprite.png')
    robot_group.add(robot)
    spawn = open('spawn.txt', 'r')
    spawning = spawn.readlines()[lines]
    spawnlist = (spawning.strip().split(','))
    spawn.close()
    RobotStats['HP']=robot.health
    RobotStats['currentXP'] = robot.exp
    RobotStats['RobotLevel']= 1
    RobotStats['MaxHP']= 50
    RobotStats['Atk']=10
    RobotStats['Armour']=0
    RobotStats['Weapon']="pistol"
    RobotStats['TargetXP']=10
    wave_text = classdefs.Text(50, (0, 0, 0), (500, 50), 0, 'Score:', 255)
    """updates all the sprites in spritegroups"""
    allSprites = pygame.sprite.OrderedUpdates \
        (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies,rocketenemies   ,
         pistolenemies, wave_text, powerups,
         explosions,statlist,bosses)
"""defining stats for first time"""
def statsetup():
    global level
    global hp
    global maxhp
    global atk
    global armour
    global weapon
    global exp
    global nextlvl
    global wavenumber
    RobotStats['HP']=robot.health
    RobotStats['currentXP'] = robot.exp
    RobotStats['RobotLevel']= 1
    RobotStats['MaxHP']= 50
    RobotStats['Atk']=10
    RobotStats['Armour']=0
    RobotStats['Weapon']="pistol"
    RobotStats['TargetXP']=10
    level = classdefs.Text(30, (0, 0, 0), (1100, 100), 0, 'Level: ', 255)
    level.set_variable(str(RobotStats['RobotLevel']))
    hp = classdefs.Text(30, (0, 0, 0), (1100, 130), 0, 'HP: ', 255)
    hp.set_variable(str(RobotStats['HP']))
    maxhp = classdefs.Text(30, (0, 0, 0), (1100, 160), 0, 'Max HP: ', 255)
    maxhp.set_variable(str(RobotStats['MaxHP']))
    atk =classdefs. Text(30, (0, 0, 0), (1100, 190), 0, 'Atack: ', 255)
    atk.set_variable(str(RobotStats['Atk']))
    armour = classdefs.Text(30, (0, 0, 0), (1100, 220), 0, 'Armour: ', 255)
    armour.set_variable(str(RobotStats['Armour']))
    weapon = classdefs.Text(30, (0, 0, 0), (1150, 250), 0, 'Weapon: ', 255)
    weapon.set_variable(str(RobotStats['Weapon']))
    exp = classdefs.Text(30, (0, 0, 0), (1100, 280), 0, 'exp: ', 255)
    exp.set_variable(str(RobotStats['currentXP']))
    nextlvl = classdefs.Text(30, (0, 0, 0), (1100, 310), 0, 'TargetXP: ', 255)
    nextlvl.set_variable(str(RobotStats['TargetXP']))
    wavenumber = classdefs.Text(30, (0, 0, 0), (1100, 340), 0, 'Wave: ', 255)
    wavenumber.set_variable(str(wave))
    statlist.add(level,hp,maxhp,atk,armour,exp,nextlvl,weapon,wavenumber)
"""updates stats at the end of every frame"""
def updatestats():
    RobotStats['HP']=robot.health
    RobotStats['currentXP'] = robot.exp
    RobotStats['Weapon'] = weapons[weaponselected-1]
    level.set_variable(str(RobotStats['RobotLevel']))
    hp.set_variable(str(RobotStats['HP']))
    maxhp.set_variable(str(RobotStats['MaxHP']))
    atk.set_variable(str(RobotStats['Atk']))
    armour.set_variable(str(RobotStats['Armour']))
    exp.set_variable(str(RobotStats['currentXP']))
    nextlvl.set_variable(str(RobotStats['TargetXP']))
    weapon.set_variable(str(RobotStats['Weapon']))
    wavenumber.set_variable(str(wave))
    if RobotStats['TargetXP']<=RobotStats['currentXP']:
        Statcalc()
        robot.exp=0
        robot.health=RobotStats['MaxHP']

def target():
    nearest = 1050
    for enemy in enemies,rocketenemies,pistolenemies,bosses:
        distance = math.sqrt \
            (pow(enemy.rect.centerx - robot.rect.centerx, 2) + pow(enemy.rect.centery - robot.rect.centery, 2))
        if distance < nearest:
            nearest = distance
            x = enemy.rect.centerx
            y = enemy.rect.centery
    if nearest <= 1000:
        firegun = (x, y, True)
        return firegun
    elif nearest == 1050:
        firegun = (0, 0, False)
        return firegun

"""clear screen and give game over message and wait for user to decide to quit or retry"""
def GameOver(score, screen):
    finalscore = classdefs.Text(50, (0, 0, 0), (750, 400), str(score), 'F i n a l   S c o r e :  ', 255)
    screen.fill([255, 255, 255])
    fs = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    fs.add(finalscore)
    button1=classdefs.button("Play Again", 570, 450, 100, 50, green, white,screen)
    button2 = classdefs.button("Quit", 870, 450, 100, 50, red, black,screen)
    buttons.add(button1)
    buttons.add(button2)
    display = pygame.sprite.OrderedUpdates \
        (fs,buttons)
    display.update()
    display.draw(screen)
    pygame.display.flip()
    x=True

    while x==True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]>= 570 and pygame.mouse.get_pos()[0]<= 620:
                    if pygame.mouse.get_pos()[1]>= 450 and pygame.mouse.get_pos()[1]<= 500:
                        x=False
                        running==True
                        reset()
                        break
                elif pygame.mouse.get_pos()[0]>= 870 and pygame.mouse.get_pos()[0]<= 920:
                    if pygame.mouse.get_pos()[1]>= 450 and pygame.mouse.get_pos()[1]<= 500:
                        sys.exit(0)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(60)
        display.update()
        display.draw(screen)
        pygame.display.flip()
wave_text = classdefs.Text(50, (0, 0, 0), (500, 50), 0, 'Score:', 255)
reset()
statsetup()
wave_text.set_variable(str(score))
i=0
x=0
allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox, robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies,rocketenemies,pistolenemies,wave_text, powerups,explosions,statlist,bosses)
"""mainloop"""
while running==True:
    clock.tick(60)
    if weaponselected!=6:
        if RobotStats['RobotLevel'] >= 5:
            gotshotgun = True
            weaponselected=2
        if RobotStats['RobotLevel'] >= 10:
            gotmachinegun = True
            weaponselected=3
        if RobotStats['RobotLevel'] >= 15:
            gotrocketlauncher = True
            weaponselected=4
        if RobotStats['RobotLevel'] >= 20:
            gotplasmarifle= True
            weaponselected=5

    firegun = target()
    """deciding which weapon selected"""
    if firegun:
        if firegun[2]:
            robot.rotate([firegun[0], firegun[1]])
            if weaponselected==1 and pygame.time.get_ticks() - lastfired >= 500:
                lastfired = pygame.time.get_ticks()
                fire.play(0)
                bullet1 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, [firegun[0], firegun[1]], 10, 2)
                tracer1 = classdefs.Bullet \
                    (None, None, robot.rect.center, [firegun[0], firegun[1]], 10, 2)
                bullet_img.add(bullet1)
                bullet_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                          robot_group, erocket_hitbox, erocket_img, rocket_hitbox,
                                                          rocket_img, enemies, rocketenemies, statlist,bosses,
                                                          pistolenemies, wave_text, powerups, explosions)
            elif gotshotgun == True and weaponselected == 2 and pygame.time.get_ticks() - lastfired >= 1200:
                lastfired = pygame.time.get_ticks()
                fireshotgun.play(0)
                bullet1 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, ([firegun[0], firegun[1]][0] + 200, [firegun[0], firegun[1]][1] + 200), 10, 7)
                tracer1 = classdefs.Bullet \
                    (None, None, robot.rect.center,
                     ([firegun[0], firegun[1]][0] + 200, [firegun[0], firegun[1]][1] + 200), 10, 7)
                bullet_img.add(bullet1)
                bullet_hitbox.add(tracer1)
                bullet2 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, [firegun[0], firegun[1]], 10, 7)
                tracer2 = classdefs.Bullet \
                    (None, None, robot.rect.center, [firegun[0], firegun[1]], 10, 7)
                bullet_img.add(bullet2)
                bullet_hitbox.add(tracer2)
                bullet3 = classdefs.Bullet \
                    (pygame.image.load('./shot.png'), robot.getangle(), \
                     robot.rect.center, ([firegun[0], firegun[1]][0] - 200, [firegun[0], firegun[1]][1] + 200), 10, 7)
                tracer3 = classdefs.Bullet \
                    (None, None, robot.rect.center,
                     ([firegun[0], firegun[1]][0] - 200, [firegun[0], firegun[1]][1] + 200), 10, 7)
                bullet_img.add(bullet3)
                bullet_hitbox.add(tracer3)

            elif gotmachinegun == True and weaponselected == 3:
                rapidfire = True
            elif gotrocketlauncher == True and weaponselected == 4 and pygame.time.get_ticks() - lastfired >= 1000:
                lastfired = pygame.time.get_ticks()
                firerocket.play(0)
                rocket = classdefs.Rocket \
                    (pygame.image.load('./rocket.png'), robot.getangle(), \
                     robot.rect.center, [firegun[0], firegun[1]], 10, 15)
                tracer1 = classdefs.Rocket \
                    (None, None, robot.rect.center, [firegun[0], firegun[1]], 10, 10)
                rocket_img.add(rocket)
                rocket_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                          robot_group, erocket_hitbox, erocket_img, rocket_hitbox,
                                                          rocket_img, enemies, rocketenemies, statlist,bosses,
                                                          pistolenemies, wave_text, powerups, explosions)
            elif gotplasmarifle == True and weaponselected == 5:
                rapidfire2 = True
            elif weaponselected==6:
                rapidfire3=True
                rapidfire4 = True
                rapidfire5 = True
        else:
            rapidfire=False
            rapidfire2 = False
            rapidfire3 = False
            rapidfire4 = False
            rapidfire5 = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.key == pygame.K_1:
                rapidfire = False
                rapidfire2 = False
                rapidfire3 = False
                rapidfire4 = False
                rapidfire5 = False
                weaponselected = 1
                robot.weapon="Pistol"
            elif event.key == pygame.K_2:
                rapidfire = False
                rapidfire2 = False
                rapidfire3 = False
                rapidfire4 = False
                rapidfire5 = False
                if gotshotgun==True:
                    weaponselected = 2
                    robot.weapon = "Shotgun"

            elif event.key == pygame.K_3:
                rapidfire = False
                rapidfire2= False
                if gotmachinegun == True:
                    weaponselected = 3
                    rapidfire = False
                    rapidfire2 = False
                    rapidfire3 = False
                    rapidfire4 = False
                    rapidfire5 = False
                    robot.weapon = "Machine Gun"


            elif event.key == pygame.K_4:
                rapidfire = False
                rapidfire2 = False
                rapidfire3 = False
                rapidfire4 = False
                rapidfire5 = False
                if gotrocketlauncher == True:
                    weaponselected = 4
                    robot.weapon = "Rocket Launcher"
            elif event.key == pygame.K_5:
                if gotplasmarifle == True:
                    weaponselected = 5
                    rapidfire = False
                    rapidfire2 = False
                    rapidfire3 = False
                    rapidfire4 = False
                    rapidfire5 = False
                    robot.weapon = "Plasma Rifle"
            elif event.key ==pygame.K_i:
                command = input('cheat: ')
                pygame.time.delay(3000)
                if command=='idios':
                    weaponselected = 6
                    rapidfire = False
                    rapidfire2 = False
                    rapidfire3 = False
                    rapidfire4 = False
                    rapidfire5 = False
                if command=='idfa':
                    gotshotgun = True
                    gotmachinegun = True
                    gotplasmarifle = True
                    gotrocketlauncher = True
                if command=='iddqd':
                    RobotStats['RobotLevel']=9999
                    robot.exp=9999
                    RobotStats['currentXP'] = 9999



        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
    """spawning enemies"""
    if i < len(spawnlist):
        x += 1
        # delay by %3
        if x % 70 == 0:
            tospawn = spawnlist[i]
            if tospawn == 'enemy':
                enemy1 = classdefs.enemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                enemies.add(enemy1)
            elif tospawn == 'penemy':
                enemy1 = classdefs.pistolenemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                pistolenemies.add(enemy1)
            elif tospawn == 'renemy':
                enemy1 = classdefs.rocketenemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                rocketenemies.add(enemy1)
            i += 1
    else:
        try:
            lines+=1
            spawn = open('spawn.txt', 'r')
            spawner=spawn.readlines()[lines]
            spawnlist=spawner.strip().split(',')
            spawn.close()
            wave += 1
            i=0
        except:
            x += 1
            # delay by %3
            if x % 201 == 0:
                enemy1 = classdefs.rocketenemy(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                rocketenemies.add(enemy1)
            if x % 1000 == 0:
                boss = classdefs.boss(pygame.image.load('./temp_sprite.png'), robot.rect.center, screen)
                bosses.add(boss)

    """dealing with autofire weapons"""
    if rapidfire:
        machinegundelay += 1
    # delay by %3
        if machinegundelay % 5 == 0:
            fire.play()
            bullet1 =classdefs.Bullet(pygame.image.load('./shot.png'), robot.getangle(), \
            robot.rect.center, [firegun[0], firegun[1]], 20,3)
            bullet2 = classdefs.Bullet(None, None, robot.rect.center, [firegun[0], firegun[1]], 10,3)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                      robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies, pistolenemies,rocketenemies   ,statlist,bosses,
                                                      wave_text, powerups, explosions)

    if rapidfire2:
        plasmarifledelay += 1
    # delay by %3
        if plasmarifledelay % 5 == 0:
                fireplasma.play()
                bullet1 = classdefs.Bullet(pygame.image.load('./plasmabolt.png'), robot.getangle(), \
                robot.rect.center, [firegun[0], firegun[1]], 7, 5)
                bullet2 = classdefs.Bullet(None, None, robot.rect.center, [firegun[0], firegun[1]], 7,5)
                bullet_img.add(bullet1)
                bullet_hitbox.add(bullet2)
                allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                          robot_group, rocket_hitbox, rocket_img,erocket_hitbox, erocket_img, enemies, pistolenemies,rocketenemies   ,statlist,bosses,
                                                          wave_text, powerups, explosions)
    if rapidfire3:
        bldelay1 += 1
        # delay by %3
        if bldelay1 % 2 == 0:
            fire.play()
            bullet1 = classdefs.Bullet(pygame.image.load('./shot.png'), robot.getangle(), \
                                       [robot.rect.centerx - 50, robot.rect.centery], [firegun[0], firegun[1]], 20, 3)
            bullet2 = classdefs.Bullet(None, None,[robot.rect.centerx-50,robot.rect.centery], [firegun[0], firegun[1]], 10, 3)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            bullet1 = classdefs.Bullet(pygame.image.load('./shot.png'), robot.getangle(), \
                                       [robot.rect.centerx+50,robot.rect.centery], [firegun[0], firegun[1]], 20, 3)
            bullet2 = classdefs.Bullet(None, None, [robot.rect.centerx+50,robot.rect.centery], [firegun[0], firegun[1]], 10, 3)
            bullet_img.add(bullet1)
            bullet_hitbox.add(bullet2)
            allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                      robot_group, rocket_hitbox, rocket_img, erocket_hitbox,
                                                      erocket_img, enemies, pistolenemies, rocketenemies, statlist,bosses,
                                                      wave_text, powerups, explosions)

    if rapidfire4:
        bldelay2 += 1
        # delay by %3
        if bldelay2 % 4 == 0:
                fireplasma.play()
                bullet1 = classdefs.Bullet(pygame.image.load('./plasmabolt.png'), robot.getangle(), \
                                           robot.rect.center, [firegun[0], firegun[1]], 7, 5)
                bullet2 = classdefs.Bullet(None, None, robot.rect.center, [firegun[0], firegun[1]], 7, 5)
                bullet_img.add(bullet1)
                bullet_hitbox.add(bullet2)
                allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                          robot_group, rocket_hitbox, rocket_img, erocket_hitbox,
                                                          erocket_img, enemies, pistolenemies, rocketenemies, statlist,bosses,
                                                          wave_text, powerups, explosions)
    if rapidfire5:
        bldelay3+= 1
        # delay by %3
        if bldelay3 % 10 == 0:
                firerocket.play()
                rocket = classdefs.Rocket \
                    (pygame.image.load('./rocket.png'), robot.getangle(), \
                     robot.rect.center, [firegun[0], firegun[1]], 10, 5)
                tracer1 = classdefs.Rocket \
                    (None, None, robot.rect.center, [firegun[0], firegun[1]], 10, 5)
                rocket_img.add(rocket)
                rocket_hitbox.add(tracer1)
                allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                          robot_group, rocket_hitbox, rocket_img, erocket_hitbox,
                                                          erocket_img, enemies, pistolenemies, rocketenemies, statlist,bosses,
                                                          wave_text, powerups, explosions)
    """enemy position and rotation update"""
    for enemy in enemies:
        allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                  erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img,
                                                  enemies, rocketenemies, statlist,bosses, pistolenemies, wave_text, powerups,
                                                  explosions)
        enemy.rotate(robot.rect.center)
        enemy.set_step_amount(robot.rect.center)
    """enemy firing timings"""
    for pistolenemy in pistolenemies:
        if pygame.time.get_ticks()-pistolenemy.getfired()>700:
            fire.play()
            bullet1 = classdefs.enemyBullet \
                (pygame.image.load('./shot.png'), pistolenemy.getangle(), \
                 pistolenemy.rect.center, robot.getpos(), 10, 5)
            tracer1 = classdefs.enemyBullet \
                (None, None, pistolenemy.rect.center, robot.getpos(), 10, 5)
            ebullet_img.add(bullet1)
            ebullet_hitbox.add(tracer1)
            allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   , statlist,bosses ,      pistolenemies, wave_text, powerups,          explosions)
            pistolenemy.setfired(pygame.time.get_ticks())
        pistolenemy.rotate(robot.rect.center)
        pistolenemy.set_step_amount(robot.rect.center)

    for bossenemy in bosses:
        if pygame.time.get_ticks()-bossenemy.getfired()>900:
            fireplasma.play()
            bullet1 = classdefs.enemyBullet \
                (pygame.image.load('./plasmabolt.png'), bossenemy.getangle(), \
                 bossenemy.rect.center, robot.getpos(), 10, 7)
            tracer1 = classdefs.enemyBullet \
                (None, None, bossenemy.rect.center, robot.getpos(), 10, 7)
            ebullet_img.add(bullet1)
            ebullet_hitbox.add(tracer1)
            bossenemy.setfired(pygame.time.get_ticks())
            allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   , statlist,bosses ,      pistolenemies, wave_text, powerups,          explosions)
        if pygame.time.get_ticks() - bossenemy.getfiredr() > 1500:
            firerocket.play()
            bullet1 = classdefs.enemyRocket \
                (pygame.image.load('./rocket.png'), bossenemy.getangle(), \
                 bossenemy.rect.center, robot.getpos(), 10, 10)
            tracer1 = classdefs.enemyRocket \
                (None, None, bossenemy.rect.center, robot.getpos(), 10, 10)
            erocket_img.add(bullet1)
            erocket_hitbox.add(tracer1)
            allSprites = pygame.sprite.OrderedUpdates(bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,
                                                      erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img,
                                                      enemies, rocketenemies, statlist, bosses, pistolenemies, wave_text,
                                                      powerups, explosions)
            bossenemy.setfiredr(pygame.time.get_ticks())
        bossenemy.rotate(robot.rect.center)
        bossenemy.set_step_amount(robot.rect.center)

    for rocketenemy in rocketenemies:
        if pygame.time.get_ticks()-rocketenemy.getfired()>700:
            firerocket.play()
            bullet1 = classdefs.enemyRocket \
                (pygame.image.load('./rocket.png'), rocketenemy.getangle(), \
                 rocketenemy.rect.center, robot.getpos(), 10, 5)
            tracer1 = classdefs.enemyRocket \
                (None, None, rocketenemy.rect.center, robot.getpos(), 10, 5)
            erocket_img.add(bullet1)
            erocket_hitbox.add(tracer1)
            allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img,ebullet_hitbox, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies , statlist,bosses   ,      pistolenemies, wave_text, powerups,          explosions)
            rocketenemy.setfired(pygame.time.get_ticks())
        rocketenemy.rotate(robot.rect.center)
        rocketenemy.set_step_amount(robot.rect.center)
    """collision detection"""
    c = pygame.sprite.groupcollide(bullet_hitbox, enemies,True, False)
    v = pygame.sprite.groupcollide(bullet_img, enemies, True, False)
    if c:
        for bullet in c.keys():
            if not (c[bullet][0].damage(bullet.getdamage()+RobotStats['Atk'])):
                robot.giveexp(c[bullet][0].givenxp)
                c[bullet][0].kill()
                score+=100
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies, statlist,bosses ,       pistolenemies, wave_text, powerups,          explosions)
    cp = pygame.sprite.groupcollide(ebullet_hitbox, robot_group, True, False)
    vp = pygame.sprite.groupcollide(ebullet_img, robot_group, True, False)
    if cp:
        for bullet in cp.keys():
            if not (cp[bullet][0].takedamage(bullet.getdamage(),screen)):
                robot.kill()
                playerdeath.play(0)
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                pain.play(0)
    cr = pygame.sprite.groupcollide(erocket_hitbox, robot_group, True, False)
    vr = pygame.sprite.groupcollide(erocket_img, robot_group, True, False)
    if cr:
        for bullet in cr.keys():
            if not (cr[bullet][0].takedamage(30,screen)):
                robot.kill()
                playerdeath.play(0)
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                pain.play(0)

    r = pygame.sprite.groupcollide(rocket_hitbox, enemies, True, False)
    s = pygame.sprite.groupcollide(rocket_img, enemies, True, False)
    if r:
        for rockets in r.keys():
            if not (r[rockets][0].damage(10+RobotStats['Atk'])):
                r[rockets][0].kill()
                explode.play(0)
                score += 100
                robot.giveexp(1)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,       statlist,bosses,     pistolenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)
    c2 = pygame.sprite.groupcollide(bullet_hitbox, pistolenemies,True, False)
    v2 = pygame.sprite.groupcollide(bullet_img, pistolenemies, True, False)
    if c2:
        for bullet in c2.keys():
            if not (c2[bullet][0].damage(bullet.getdamage()+RobotStats['Atk'])):
                c2[bullet][0].kill()
                score += 100
                robot.giveexp(2)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,   statlist,bosses  ,      pistolenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)
    r2 = pygame.sprite.groupcollide(rocket_hitbox, pistolenemies, True, False)
    s2 = pygame.sprite.groupcollide(rocket_img, pistolenemies, True, False)
    if r:
        for rockets in r2.keys():
            if not (r2[rockets][0].damage(10+RobotStats['Atk'])):
                r2[rockets][0].kill()
                explode.play(0)
                score += 100
                robot.giveexp(2)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,       statlist,bosses  ,   pistolenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)
    c3 = pygame.sprite.groupcollide(bullet_hitbox, rocketenemies,True, False)
    v3 = pygame.sprite.groupcollide(bullet_img, rocketenemies, True, False)
    if c3:
        for bullet in c3.keys():
            if not (c3[bullet][0].damage(bullet.getdamage()+RobotStats['Atk'])):
                c3[bullet][0].kill()
                score+=100
                robot.giveexp(10)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,    statlist,bosses   ,     rocketenemies, wave_text, powerups,          explosions)
    b4 = pygame.sprite.groupcollide(rocket_hitbox, bosses, True, False)
    b5 = pygame.sprite.groupcollide(rocket_img, bosses, True, False)
    if b4:
        for rockets in b4.keys():
            if not (b4[rockets][0].damage(10+RobotStats['Atk'])):
                b4[rockets][0].kill()
                explode.play(0)
                score += 1000
                robot.giveexp(50)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,  statlist,bosses  ,       rocketenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)
    b = pygame.sprite.groupcollide(bullet_hitbox, bosses,True, False)
    b2 = pygame.sprite.groupcollide(bullet_img, bosses, True, False)
    if b:
        for bullet in b.keys():
            if not (b[bullet][0].damage(bullet.getdamage()+RobotStats['Atk'])):
                b[bullet][0].kill()
                score+=1000
                robot.giveexp(50)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies,rocketenemies   ,    statlist,bosses   ,     rocketenemies, wave_text, powerups,          explosions)
    r4 = pygame.sprite.groupcollide(rocket_hitbox, rocketenemies, True, False)
    s4 = pygame.sprite.groupcollide(rocket_img, rocketenemies, True, False)
    if r4:
        for rockets in r4.keys():
            if not (r4[rockets][0].damage(10+RobotStats['Atk'])):
                r4[rockets][0].kill()
                explode.play(0)
                score += 100
                robot.giveexp(10)
                allSprites = pygame.sprite.OrderedUpdates (bullet_img, bullet_hitbox, ebullet_img, ebullet_hitbox,erocket_hitbox, erocket_img, robot_group, rocket_hitbox, rocket_img, enemies, rocketenemies   ,  statlist,bosses  ,       rocketenemies, wave_text, powerups,          explosions)
            else:
                explode.play(0)


    e = pygame.sprite.groupcollide(enemies,robot_group,False,False)
    if e:
        for rockets in e.keys():
            if not (robot.takedamage(5,screen)):
                robot.kill()
                playerdeath.play(0)
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                score -= 10
                pain.play(0)
    pp = pygame.sprite.groupcollide(pistolenemies,robot_group,False,False)
    if pp:
        for rockets in pp.keys():
            if not (robot.takedamage(5,screen)):
                robot.kill()
                playerdeath.play(0)
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                score -= 10
                pain.play(0)
    bb = pygame.sprite.groupcollide(bosses,robot_group,True,False)
    if bb:
        for rockets in bb.keys():
            if not (robot.takedamage(200,screen)):
                robot.kill()
                playerdeath.play(0)
                screen.fill([255,255,255])
                GameOver(score,screen)
            else:
                score -= 300
                pain.play(0)


    wave_text.set_variable(str(score))
    screen.fill([255,255,255])
    updatestats()
    screen.blit(spritebg, (1024, 0))
    allSprites.update()
    allSprites.draw(screen)
    pygame.display.flip()
