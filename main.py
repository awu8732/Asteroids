import pygame
import random
import time

import globals
import Game
from Button import Button
from Coin import Coin
from Asteroid import Asteroid
from Laser import Laser

aHit = {0: [67, 88, 13, 3], 1: [48, 62, 9, 2], 2: [81, 81, 9, 6], 3: [49, 49, 4, 6],
        4: [81, 105, 0, 0], 5: [40, 53, 0, 0], 6: [49, 40, 24, 9]}

clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 50, True)
sfont = pygame.font.SysFont('comicsans', 50, True)
dfont = pygame.font.SysFont('comicsans', 100, True)
rfont = pygame.font.SysFont('comicsans', 10)
bfont = pygame.font.SysFont('comicsans', 50, True)
bfont2 = pygame.font.SysFont('comicsans', 25, True)
text2 = dfont.render('YOU DIED!', 1, (139, 0, 0))
now1 = time.time()
clicked = 0
speed = 8
laserSpeed = 30
speedbar = 0
bspeedbar = 0
upgrade = False
bupgrade = False

starx = []
stary = []

#//////////////////////////////////////////////////////////////////////////functions
def drawGameWin():
    Game.WIN.blit(globals.BACKGROUND_IMAGE, (0, 0))
    Game.USER.draw(Game.WIN)
    for asteroid in Game.ONSCREEN_ASTEROIDS:
        asteroid.draw(Game.WIN)
    for coin in Game.ONSCREEN_COINS:
        coin.draw(Game.WIN)
    for laser in Game.ONSCREEN_LASERS:
        laser.draw(Game.WIN)
    text = font.render('Coins: ' + str(globals.CURRENT_COIN_COUNT), 1, (255, 255, 255))
    Game.WIN.blit(text, (795, 70))
    text1 = sfont.render('Score: ' + str(globals.CURRENT_SCORE), 1, (255, 255, 255))
    Game.WIN.blit(text1, (795, 10))
    btext = bfont.render('Best Score: ' + str(globals.CURRENT_BEST_SCORE), 1, (255, 255, 255))
    Game.WIN.blit(btext, (700, 130))

    pygame.display.update()
def Screen1():
    Game.WIN.fill((0, 0, 0))
    for i in range(200):
        pygame.draw.circle(Game.WIN, (255, 255, 255), (starx[i], stary[i]), 1)
    Game.PLAY_BUTTON.draw(Game.WIN)
    Game.STORE_BUTTON.draw(Game.WIN)
    btext2 = bfont2.render('Best Score: ' + str(globals.CURRENT_BEST_SCORE), 1, (255, 255, 255))
    Game.WIN.blit(btext2, (700, 10))
    Game.WIN.blit(globals.LOGO_IMAGE, (136, 180))
    displaycoins = bfont2.render('Coins: ' + str(globals.CURRENT_COIN_COUNT), 1, (255, 255, 255))
    Game.WIN.blit(displaycoins, (700, 40))

def Store():
    Game.USER.speed = 8
    bigfont = pygame.font.SysFont('comicsans', 50, True)
    Game.WIN.fill((139, 134, 130))
    Game.BACK_BUTTON.draw(Game.WIN)
    for p in range(3):
        pygame.draw.rect(Game.WIN, (91, 91, 91), (550, 111 + 163 * p, 400, 142))
        pygame.draw.rect(Game.WIN, (0, 0, 0), (550, 111 + 85 + 163 * p, 300, 57), 3)
        pygame.draw.rect(Game.WIN, (124, 252, 0), (850, 111 + 163 * p, 100, 142), 3)
        pygame.draw.rect(Game.WIN, (91, 91, 91), (50, 111 + 163 * p, 400, 142))
        pygame.draw.rect(Game.WIN, (0, 0, 0), (50, 111 + 85 + 163 * p, 300, 57), 3)
        pygame.draw.rect(Game.WIN, (124, 252, 0), (350, 111 + 163 * p, 100, 142), 3)
    #speed bar

    if (speed - 5)/3 <= 5:
        pygame.draw.rect(Game.WIN, (0, 191, 255), (50, 111 + 85, (speed - 5)/3 * 50, 57))
        upgradespeed.draw(Game.WIN)
    else:
        pygame.draw.rect(Game.WIN, (0, 191, 255), (50, 111 + 85, 6 * 50, 57))
        upgradespeed.text = "MAX"
        upgradespeed.draw(Game.WIN)
    #bspeed bar
    if (laserSpeed - 20)/10 <= 5:
        pygame.draw.rect(Game.WIN, (0, 191, 255), (50, 111 + 85*3-7, (laserSpeed - 20)/10 * 50, 57))
        upgradebspeed.draw(Game.WIN)
    else:
        pygame.draw.rect(Game.WIN, (0, 191, 255), (50, 111 + 85*3-7, 6 * 50, 57))
        upgradebspeed.text = "MAX"
        upgradebspeed.draw(Game.WIN)


    for x in range(3):
        for i in range(5):
            pygame.draw.line(Game.WIN, (0, 0, 0), (600 + 50 * i, 111 + 142 + 163 * x), (600 + 50 * i, 111 + 85 + 163 * x), 3)
            pygame.draw.line(Game.WIN, (0, 0, 0), (100 + 50*i, 111 + 142 + 163*x), (100 + 50*i, 111 + 85 + 163*x), 3)
    cointxt = bigfont.render('Coins: ' + str(globals.CURRENT_COIN_COUNT), 1, (255, 255, 255))
    speedtxt = bigfont.render('Speed', 1, (255, 255, 255))
    bspeedtxt = bigfont.render('Bullet Speed', 1, (255, 255, 255))
    bdmgtxt  = bigfont.render('Bullet Damage', 1, (255, 255, 255))
    reloadtxt = bigfont.render('Reload Time', 1, (255, 255, 255))
    mctxt = bigfont.render('Mag. Capacity', 1, (255, 255, 255))
    mreloadtxt = bigfont.render('Mag. Reload', 1, (255, 255, 255))
    Game.WIN.blit(cointxt, (780, 30))
    Game.WIN.blit(speedtxt, (50 + 95, 121))
    Game.WIN.blit(bspeedtxt, (50 + 30, 121 + 163))
    Game.WIN.blit(bdmgtxt, (50 + 15, 121 + 163 * 2))
    Game.WIN.blit(reloadtxt, (550 + 25, 121))
    Game.WIN.blit(mctxt, (550 + 10, 121 + 163))
    Game.WIN.blit(mreloadtxt, (550 + 25, 121 + 163 * 2))
    buttonProp(Game.BACK_BUTTON)
    pygame.display.update()

def buttonProp(button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button.isPressed(pos):
            pass
    if event.type == pygame.MOUSEMOTION:
        if button.isPressed(pos):
            button.color = (141, 238, 238)
        else:
            button.color = (0, 191, 255)

def generateStars():
    for i in range(200):
        x = random.randint(0, 1000)
        starx.append(x)
        y = random.randint(0, 600)
        stary.append(y)

def renderAmmoBar():
    if Game.USER.ammo > 0:
            pygame.draw.rect(Game.WIN, (0, 0, 0), (10, 560, globals.AMMO_BAR_WIDTH, globals.AMMO_BAR_LENGTH))
            pygame.draw.rect(Game.WIN, Game.getAmmoBarColor(), (10, 560, Game.USER.ammo/Game.USER.maxAmmo * globals.AMMO_BAR_WIDTH, globals.AMMO_BAR_LENGTH))
    else:
        #reload state
        if time.time() - now1 > 5:
            Game.USER.ammo = Game.USER.maxAmmo
        else:
            text3 = font.render('Reloading...', 1, (255, 255, 255))
            Game.WIN.blit(text3, (10, 560))
    pygame.display.update()

generateStars()
#///////////////////////////////////////////////////////////////////main
while Game.CURRENT_STATE != globals.GAME_QUIT:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.CURRENT_STATE = globals.GAME_QUIT
            break
    if Game.CURRENT_STATE == globals.HOME_STATE:
        pos = pygame.mouse.get_pos()
        Screen1()
        buttonProp(Game.PLAY_BUTTON)
        buttonProp(Game.STORE_BUTTON)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Game.PLAY_BUTTON.isPressed(pos):
                Game.CURRENT_STATE = globals.GAME_STATE
            if Game.STORE_BUTTON.isPressed(pos):
                Game.CURRENT_STATE = globals.STORE_STATE
        pygame.display.update()
    elif Game.CURRENT_STATE == globals.STORE_STATE:
        if speedbar < 5:
            upgradespeed = Button((124, 252, 0), 350, 111, 100, 142, "Cost: " + str(globals.ATTRIBUTE_UPGRADE_COSTS[speedbar]), 30)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if upgradespeed.isPressed(pos):
                    if clicked < 1:
                        upgrade = True
                        clicked += 1
                        now2 = time.time()
                    if time.time() - now2 > .2:
                        clicked = 0
                if upgrade == True:
                    if globals.CURRENT_COIN_COUNT >= globals.ATTRIBUTE_UPGRADE_COSTS[speedbar]:
                        speed += 3
                        globals.CURRENT_COIN_COUNT -= globals.ATTRIBUTE_UPGRADE_COSTS[speedbar]
                        speedbar += 1
                    upgrade = False
        if bspeedbar < 5:
            upgradebspeed = Button((124, 252, 0), 350, 111 + 85*2-5, 100, 142, "Cost: " + str(globals.ATTRIBUTE_UPGRADE_COSTS[bspeedbar]), 30)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if upgradebspeed.isPressed(pos):
                    if clicked < 1:
                        bupgrade = True
                        clicked += 1
                        now2 = time.time()
                    if time.time() - now2 > .2:
                        clicked = 0
                if bupgrade == True:
                    if globals.CURRENT_COIN_COUNT >= globals.ATTRIBUTE_UPGRADE_COSTS[bspeedbar]:
                        laserSpeed += 10
                        globals.CURRENT_COIN_COUNT -= globals.ATTRIBUTE_UPGRADE_COSTS[bspeedbar]
                        bspeedbar += 1
                    bupgrade = False
        Store()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Game.BACK_BUTTON.isPressed(pos):
                    Game.CURRENT_STATE = globals.HOME_STATE
    elif Game.CURRENT_STATE == globals.GAME_STATE:
        
        #Handle user movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and Game.USER.x + Game.USER.speed < 935:
            Game.USER.x += Game.USER.speed
        elif keys[pygame.K_LEFT] and Game.USER.x > 0:
            Game.USER.x -= Game.USER.speed
        if keys[pygame.K_DOWN] and Game.USER.y + Game.USER.speed < 550:
            Game.USER.y += Game.USER.speed
        elif keys[pygame.K_UP] and Game.USER.y - Game.USER.speed > 0:
            Game.USER.y -= Game.USER.speed
        #Handle user blasters
        if keys[pygame.K_SPACE] and Game.USER.ammo > 0:
            Game.ONSCREEN_LASERS.append(Laser(Game.USER.x + 18.5, Game.USER.y + 57))
            Game.ONSCREEN_LASERS.append(Laser(Game.USER.x + 58.5, Game.USER.y + 57))
            now1 = time.time()
            Game.USER.ammo -= 2

        Game.WIN.blit(globals.BACKGROUND_IMAGE, (0, 0))
        drawGameWin()

        renderAmmoBar()
        Game.updateOnscreenUIElements()
        if len(Game.ONSCREEN_ASTEROIDS) < 9:
            Game.ONSCREEN_ASTEROIDS.append(Asteroid())
        if len(Game.ONSCREEN_COINS) < 2:
            Game.ONSCREEN_COINS.append(Coin())
        
        counter = 0
        for money in Game.ONSCREEN_COINS:
            if Game.USER.x < money.x +7.5 < Game.USER.x +75 and Game.USER.y + 2.5 < money.y + 7.5 < Game.USER.y + 75:
                globals.CURRENT_COIN_COUNT += 1
                globals.CURRENT_SCORE += 1
                Game.ONSCREEN_COINS.pop(Game.ONSCREEN_COINS.index(money))
        for asteroid in Game.ONSCREEN_ASTEROIDS:
            for laser in Game.ONSCREEN_LASERS:
                if asteroid.x + aHit[asteroid.chose][2] < laser.x < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0]:
                    if asteroid.y + aHit[asteroid.chose][3] < laser.y < asteroid.y + aHit[asteroid.chose][3] +  aHit[asteroid.chose][1]:
                        Game.ONSCREEN_LASERS.pop(Game.ONSCREEN_LASERS.index(laser))
                        globals.CURRENT_SCORE += 5
                        try:
                            Game.ONSCREEN_ASTEROIDS.pop(Game.ONSCREEN_ASTEROIDS.index(asteroid))
                        except ValueError:
                          pass
        for asteroid in Game.ONSCREEN_ASTEROIDS:
            if asteroid.x + aHit[asteroid.chose][2] < Game.USER.x < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0] or asteroid.x + aHit[asteroid.chose][2] < Game.USER.x + 75< asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0]:
                if asteroid.y + aHit[asteroid.chose][3] < Game.USER.y + 59.5< asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1] or asteroid.y + aHit[asteroid.chose][3] < Game.USER.y + 75 < asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1]:
                    Game.handleUserDeath()
                    Game.CURRENT_STATE = globals.HOME_STATE
            elif asteroid.x + aHit[asteroid.chose][2] < Game.USER.x + 27.5 < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0] or asteroid.x + aHit[asteroid.chose][2] < Game.USER.x + 47.5 < asteroid.x + aHit[asteroid.chose][2] + aHit[asteroid.chose][0]:
                if asteroid.y + aHit[asteroid.chose][3] < Game.USER.y + 2.5 < asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1] or asteroid.y + aHit[asteroid.chose][3] < Game.USER.y + 75 < asteroid.y + aHit[asteroid.chose][3] + aHit[asteroid.chose][1]:
                    Game.handleUserDeath()
                    Game.CURRENT_STATE = globals.HOME_STATE
        clock.tick(100)

pygame.quit()


def main():
    print("hello")
    return 0

if __name__ == '__main__':
    main()