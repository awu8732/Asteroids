import pygame
import random
import time
import datetime

from Button import Button
from Coin import Coin
from Asteroid import Asteroid
from Laser import Laser
from Player import Player

aHit = {0: [67, 88, 13, 3], 1: [48, 62, 9, 2], 2: [81, 81, 9, 6], 3: [49, 49, 4, 6],
        4: [81, 105, 0, 0], 5: [40, 53, 0, 0], 6: [49, 40, 24, 9]}
costs = [5, 10, 15, 20, 25]

pygame.init()

win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Asteroids")

asteroids = [pygame.image.load('Pictures/Asteroid11.png'), pygame.image.load('Pictures/Asteroid12.png'),
             pygame.image.load('Pictures/Asteroid21.png'), pygame.image.load('Pictures/Asteroid22.png'),
             pygame.image.load('Pictures/Asteroid31.png'), pygame.image.load('Pictures/Asteroid32.png'),
             pygame.image.load('Pictures/Asteroid42.png')]
ship = pygame.image.load('Pictures/fighter.png')
logo = pygame.image.load('Pictures/Logo.png')
coin = pygame.image.load('Pictures/coin.png')
bg = pygame.image.load('Pictures/space.png')


clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 50, True)
sfont = pygame.font.SysFont('comicsans', 50, True)
dfont = pygame.font.SysFont('comicsans', 100, True)
rfont = pygame.font.SysFont('comicsans', 10)
bfont = pygame.font.SysFont('comicsans', 50, True)
bfont2 = pygame.font.SysFont('comicsans', 25, True)
text2 = dfont.render('YOU DIED!', 1, (139, 0, 0))
user = Player(400, 250, 24)
screen1 = True
store = False
run = False
game = True
button1 = Button((0, 191, 255), 400, 300, 200, 100, "PLAY")
button2 = Button((0, 191, 255), 400, 415, 200, 100, "STORE")
back = Button((0, 191, 255), 20, 20, 100, 50, "Back")
screenAsteroids = []
screenCoins = []
screenlaser = []
now1 = time.time()
bscore = 0
score = 0
coins = 100
spawnLoop = 0
spawnLoop1 = 0
spawnLoop2 = 0
magcounter = 0
clicked = 0
speed = 8
bspeed = 30
speedbar = 0
bspeedbar = 0
upgrade = False
bupgrade = False

starx = []
stary = []

#//////////////////////////////////////////////////////////////////////////functions
def drawGameWin():
    win.blit(bg, (0, 0))
    user.draw(win)
    for asteroid in screenAsteroids:
        asteroid.draw(win)

    for money in screenCoins:
        money.draw(win)

    for laser in screenlaser:
        laser.draw(win)
    text = font.render('Coins: ' + str(coins), 1, (255, 255, 255))
    win.blit(text, (795, 70))
    text1 = sfont.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(text1, (795, 10))
    btext = bfont.render('Best Score: ' + str(bscore), 1, (255, 255, 255))
    win.blit(btext, (700, 130))

    pygame.display.update()


def Screen1():
    win.fill((0, 0, 0))
    for i in range(200):
        pygame.draw.circle(win, (255, 255, 255), (starx[i], stary[i]), 1)
    button1.draw(win)
    button2.draw(win)
    btext2 = bfont2.render('Best Score: ' + str(bscore), 1, (255, 255, 255))
    win.blit(btext2, (700, 10))
    win.blit(logo, (136, 180))
    displaycoins = bfont2.render('Coins: ' + str(coins), 1, (255, 255, 255))
    win.blit(displaycoins, (700, 40))

def Store():
    user.vel = 8
    bigfont = pygame.font.SysFont('comicsans', 50, True)
    smallfont = pygame.font.SysFont('comicsans', 20)
    win.fill((139, 134, 130))
    back.draw(win)
    for p in range(3):
        pygame.draw.rect(win, (91, 91, 91), (550, 111 + 163 * p, 400, 142))
        pygame.draw.rect(win, (0, 0, 0), (550, 111 + 85 + 163 * p, 300, 57), 3)
        pygame.draw.rect(win, (124, 252, 0), (850, 111 + 163 * p, 100, 142), 3)
        pygame.draw.rect(win, (91, 91, 91), (50, 111 + 163 * p, 400, 142))
        pygame.draw.rect(win, (0, 0, 0), (50, 111 + 85 + 163 * p, 300, 57), 3)
        pygame.draw.rect(win, (124, 252, 0), (350, 111 + 163 * p, 100, 142), 3)
    #speed bar

    if (speed - 5)/3 <= 5:
        pygame.draw.rect(win, (0, 191, 255), (50, 111 + 85, (speed - 5)/3 * 50, 57))
        upgradespeed.draw(win)
    else:
        pygame.draw.rect(win, (0, 191, 255), (50, 111 + 85, 6 * 50, 57))
        upgradespeed.text = "MAX"
        upgradespeed.draw(win)
    #bspeed bar

    if (bspeed - 20)/10 <= 5:
        pygame.draw.rect(win, (0, 191, 255), (50, 111 + 85*3-7, (bspeed - 20)/10 * 50, 57))
        upgradebspeed.draw(win)
    else:
        pygame.draw.rect(win, (0, 191, 255), (50, 111 + 85*3-7, 6 * 50, 57))
        upgradebspeed.text = "MAX"
        upgradebspeed.draw(win)


    for x in range(3):
        for i in range(5):
            pygame.draw.line(win, (0, 0, 0), (600 + 50 * i, 111 + 142 + 163 * x), (600 + 50 * i, 111 + 85 + 163 * x), 3)
            pygame.draw.line(win, (0, 0, 0), (100 + 50*i, 111 + 142 + 163*x), (100 + 50*i, 111 + 85 + 163*x), 3)
    cointxt = bigfont.render('Coins: ' + str(coins), 1, (255, 255, 255))
    speedtxt = bigfont.render('Speed', 1, (255, 255, 255))
    bspeedtxt = bigfont.render('Bullet Speed', 1, (255, 255, 255))
    bdmgtxt  = bigfont.render('Bullet Damage', 1, (255, 255, 255))
    reloadtxt = bigfont.render('Reload Time', 1, (255, 255, 255))
    mctxt = bigfont.render('Mag. Capacity', 1, (255, 255, 255))
    mreloadtxt = bigfont.render('Mag. Reload', 1, (255, 255, 255))
    win.blit(cointxt, (780, 30))
    win.blit(speedtxt, (50 + 95, 121))
    win.blit(bspeedtxt, (50 + 30, 121 + 163))
    win.blit(bdmgtxt, (50 + 15, 121 + 163 * 2))
    win.blit(reloadtxt, (550 + 25, 121))
    win.blit(mctxt, (550 + 10, 121 + 163))
    win.blit(mreloadtxt, (550 + 25, 121 + 163 * 2))
    buttonProp(back)
    pygame.display.update()

def loop(name):
    if name > 0:
        name += 1
    if name > 3:
        name = 0

def buttonProp(button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button.isPressed(pos):
            pass
    if event.type == pygame.MOUSEMOTION:
        if button.isPressed(pos):
            button.color = (141, 238, 238)
        else:
            button.color = (0, 191, 255)


for i in range(200):
    x = random.randint(0, 1000)
    starx.append(x)
    y = random.randint(0, 600)
    stary.append(y)
#///////////////////////////////////////////////////////////////////main
while game:
    pygame.time.delay(25)
    while screen1:
        pygame.time.delay(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen1 = False
                game = False
        pos = pygame.mouse.get_pos()

        loop(spawnLoop)
        loop(spawnLoop1)
        if spawnLoop2 > 0:
            spawnLoop2 += 1
        if spawnLoop2 > 3:
            spawnLoop2 = 0

        Screen1()
        buttonProp(button1)
        buttonProp(button2)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.isPressed(pos):
                run = True
                screen1 = False
                store = False
            if button2.isPressed(pos):
                store = True
                screen1 = False
                run = False
        pygame.display.update()
    while store:
        if speedbar < 5:
            upgradespeed = Button((124, 252, 0), 350, 111, 100, 142, "Cost: " + str(costs[speedbar]), 30)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if upgradespeed.isPressed(pos):
                    if clicked < 1:
                        upgrade = True
                        clicked += 1
                        now2 = time.time()
                    if time.time() - now2 > .2:
                        clicked = 0
                if upgrade == True:
                    if coins >= costs[speedbar]:
                        speed += 3
                        coins -= costs[speedbar]
                        speedbar += 1
                    upgrade = False
        if bspeedbar < 5:
            upgradebspeed = Button((124, 252, 0), 350, 111 + 85*2-5, 100, 142, "Cost: " + str(costs[bspeedbar]), 30)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if upgradebspeed.isPressed(pos):
                    if clicked < 1:
                        bupgrade = True
                        clicked += 1
                        now2 = time.time()
                    if time.time() - now2 > .2:
                        clicked = 0
                if bupgrade == True:
                    if coins >= costs[bspeedbar]:
                        bspeed += 10
                        coins -= costs[bspeedbar]
                        bspeedbar += 1
                    bupgrade = False
        Store()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                store = False
                game = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back.isPressed(pos):
                store = False
                screen1 = True
                run = False
    while run:
        pygame.time.delay(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game = False
        user.vel = speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and user.x + user.vel < 935:
            user.x += user.vel
        if keys[pygame.K_LEFT] and user.x > 0:
            user.x -= user.vel
        if keys[pygame.K_DOWN] and user.y + user.vel < 550:
            user.y += user.vel
        if keys[pygame.K_UP] and user.y - user.vel > 0:
            user.y -= user.vel

        buttonProp(button1)
        win.blit(bg, (0, 0))
        drawGameWin()


        if magcounter < user.magsize:
            pygame.draw.rect(win, (0, 0, 0), (10, 560, 100, 20))
            if 1 - magcounter/user.magsize >= 0:
                color = (255, 0, 0)
                if 1 - magcounter/user.magsize >= .33:
                    color = (255, 215, 0)
                    if 1 - magcounter/user.magsize >= .54:
                        color = (173, 255, 47)
                        if 1 - magcounter/user.magsize >= .75:
                            color = (0, 255, 0)
            pygame.draw.rect(win, color, (10, 560, (1 - magcounter/user.magsize) * 100, 20))
            pygame.display.update()
            if keys[pygame.K_SPACE]:
                now2 = time.time()
                screenlaser.append(Laser(user.x + 18.5, user.y + 57))
                screenlaser.append(Laser(user.x + 58.5, user.y + 57))
                now1 = time.time()
                magcounter += 2
        else:
            if time.time() - now1 > 5:
                magcounter = 0
            else:
                text3 = font.render('Reloading...', 1, (255, 255, 255))
                win.blit(text3, (10, 560))
                pygame.display.update()
            spawnLoop2 = 0
        for laser in screenlaser:
            if laser.y > 0:
                laser.y -= bspeed
            else:
                screenlaser.pop(screenlaser.index(laser))

        if len(screenCoins) < 2:
            screenCoins.append(Coin())
            spawnLoop1 = 0
        for money in screenCoins:
            if money.y < 600:
                money.y += money.vel
            else:
                screenCoins.pop(screenCoins.index(money))

        if len(screenAsteroids) < 9:
            screenAsteroids.append(Asteroid())
            spawnLoop = 0
        for asteroid in screenAsteroids:
            if asteroid.y < 600:
                asteroid.y += asteroid.vel
            else:
                screenAsteroids.pop(screenAsteroids.index(asteroid))
        counter = 0
        for money in screenCoins:
            if user.x < money.x +7.5 < user.x +75 and user.y + 2.5 < money.y + 7.5 < user.y + 75:
                coins += 1
                score += 1
                screenCoins.pop(screenCoins.index(money))
        for asteroid in screenAsteroids:
            for laser in screenlaser:
                if asteroid.x + aHit[asteroid.chose][2] < laser.x < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0]:
                    if asteroid.y + aHit[asteroid.chose][3] < laser.y < asteroid.y + aHit[asteroid.chose][3] +  aHit[asteroid.chose][1]:
                        screenlaser.pop(screenlaser.index(laser))
                        score += 5
                        try:
                            screenAsteroids.pop(screenAsteroids.index(asteroid))
                        except ValueError:
                          pass
        for asteroid in screenAsteroids:
            if asteroid.x + aHit[asteroid.chose][2] < user.x < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0] or asteroid.x + aHit[asteroid.chose][2] < user.x + 75< asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0]:
                if asteroid.y + aHit[asteroid.chose][3] < user.y + 59.5< asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1] or asteroid.y + aHit[asteroid.chose][3] < user.y + 75 < asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1]:
                    if score > bscore:
                        bscore = score
                    score = 0
                    screenAsteroids = []
                    screenCoins = []
                    screenlaser = []
                    user.x = 400
                    user.y = 250
                    magcounter = 0

                    now = time.time()
                    future = now + 3
                    while time.time() < future:
                        win.blit(text2, (300, 300))
                        pygame.display.update()
                    run = False
                    screen1 = True
            elif asteroid.x + aHit[asteroid.chose][2] < user.x + 27.5 < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0] or asteroid.x + aHit[asteroid.chose][2] < user.x + 47.5 < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0]:
                if asteroid.y + aHit[asteroid.chose][3] < user.y + 2.5 < asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1] or asteroid.y + aHit[asteroid.chose][3] < user.y + 75 < asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1]:
                    if score > bscore:
                        bscore = score
                    score = 0
                    screenAsteroids = []
                    screenCoins = []
                    screenlaser = []
                    user.x = 400
                    user.y = 250
                    magcounter = 0

                    now = time.time()
                    future = now + 3
                    while time.time() < future:
                        win.blit(text2, (300, 300))
                        pygame.display.update()
                    run = False
                    screen1 = True

        clock.tick(100)



pygame.quit()
