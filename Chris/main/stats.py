from random import randint
import pygame,pygame.locals

pygame.font.init()

RobotStats = {
    'RobotLevel': 1,
    'MaxHP': 50,
    'HP': 50,
    'Atk': 10,
    'Armour': 0,
    'Weapon': "",
   ## 'AtkRng': 100,,
    'currentXP':0,
    'TargetXP':10
}


StatCalc = randint(0, 2)
if StatCalc == 0:
    StatCalc = 60
elif StatCalc == 1:
    StatCalc = 70
elif StatCalc == 2:
    StatCalc = 80

AtkStatCalc = StatCalc + randint(-5,5)
ArmourStatCalc = StatCalc + randint(-5,5)


BonusStat = randint(5,16)
BonusHPStat = randint(50,76)

def Statcalc():
    #Calculating Stats
    RobotStats['RobotLevel'] +=1
    #MaxHP
    RobotStats['MaxHP'] += (round(((StatCalc * 2) * RobotStats['RobotLevel']) / 100 + BonusHPStat))
    ##HP
    RobotStats['HP'] = (RobotStats['MaxHP'])
    #Attack Stat
    RobotStats['Atk'] = round(((AtkStatCalc * 3.25) * RobotStats['RobotLevel']) / 100 + BonusStat) # add or multiply by weapon damage??
    #Armour Stat
    RobotStats['Armour'] = round(((ArmourStatCalc * 3.25) * RobotStats['RobotLevel']) / 100 + BonusStat) # add by equipped custom armour ??
    #EXP
    RobotStats['currentXP'] = 0
    #EXP to next level
    RobotStats['TargetXP'] = RobotStats['RobotLevel']*10