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
def Store():
    Game.WIN.fill((127, 137, 143))
    Game.BACK_BUTTON.draw(Game.WIN)

    leftMargin = globals.GAME_WINDOW_WIDTH/10
    padding = 5
    attrSize = 60
    for i, attribute in enumerate(globals.UPGRADE_ATTRIBUTES):
        attributeText = globals.NORMAL_FONT.render(attribute , 1, globals.WHITE)
        Game.WIN.blit(attributeText, (leftMargin, 75 + 80 * i))
        pygame.draw.rect(Game.WIN, globals.WHITE, (leftMargin, 100 + 80 * i, globals.GAME_WINDOW_WIDTH*2/3, 50))
        globals.UPGRADE_ATTRIBUTES[attribute][3].draw(Game.WIN)

        currentLevel = globals.UPGRADE_ATTRIBUTES[attribute][1]
        for j in range(currentLevel + 1):
            pygame.draw.rect(Game.WIN, (63, 159, 217), (leftMargin + padding + (attrSize + padding) * j, 100 + 80 * i + padding, attrSize, 50 - 2 * padding))
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
            isReloadingText = globals.STAT_FONT.render('Reloading...', 1, (255, 255, 255))
            Game.WIN.blit(isReloadingText, (10, globals.GAME_WINDOW_LENGTH - 40))
    pygame.display.update()

generateStars()
#///////////////////////////////////////////////////////////////////main
while Game.CURRENT_STATE != globals.GAME_QUIT:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.CURRENT_STATE = globals.GAME_QUIT
            break
        elif event.type == pygame.VIDEORESIZE:
            globals.GAME_WINDOW_WIDTH = event.w
            globals.GAME_WINDOW_LENGTH = event.h
            Game.WIN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            pygame.display.flip()

    if Game.CURRENT_STATE == globals.HOME_STATE:
        pos = pygame.mouse.get_pos()
        Game.renderHomeScreen()
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
        Game.renderStoreScreen()
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
        if keys[pygame.K_SPACE]:
            Game.ONSCREEN_LASERS.append(Laser(Game.USER.x + 18.5, Game.USER.y + 57))
            Game.ONSCREEN_LASERS.append(Laser(Game.USER.x + 58.5, Game.USER.y + 57))
            now1 = time.time() #############
            Game.USER.ammo -= 2

        Game.WIN.blit(globals.BACKGROUND_IMAGE, (0, 0))
        Game.renderGameScreen()

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
                if asteroid.x + aHit[asteroid.type][2] < laser.x < asteroid.x + aHit[asteroid.type][2] + aHit[asteroid.type][0]:
                    if asteroid.y + aHit[asteroid.type][3] < laser.y < asteroid.y + aHit[asteroid.type][3] +  aHit[asteroid.type][1]:
                        Game.ONSCREEN_LASERS.pop(Game.ONSCREEN_LASERS.index(laser))
                        globals.CURRENT_SCORE += 5
                        try:
                            Game.ONSCREEN_ASTEROIDS.pop(Game.ONSCREEN_ASTEROIDS.index(asteroid))
                        except ValueError:
                          pass
        for asteroid in Game.ONSCREEN_ASTEROIDS:
            if asteroid.x + aHit[asteroid.type][2] < Game.USER.x < asteroid.x + aHit[asteroid.type][2] + aHit[asteroid.type][0] or asteroid.x + aHit[asteroid.type][2] < Game.USER.x + 75< asteroid.x + aHit[asteroid.type][2] + aHit[asteroid.type][0]:
                if asteroid.y + aHit[asteroid.type][3] < Game.USER.y + 59.5< asteroid.y + aHit[asteroid.type][3] + aHit[asteroid.type][1] or asteroid.y + aHit[asteroid.type][3] < Game.USER.y + 75 < asteroid.y + aHit[asteroid.type][3] + aHit[asteroid.type][1]:
                    Game.handleUserDeath()
                    Game.CURRENT_STATE = globals.HOME_STATE
            elif asteroid.x + aHit[asteroid.type][2] < Game.USER.x + 27.5 < asteroid.x + aHit[asteroid.type][2] + aHit[asteroid.type][0] or asteroid.x + aHit[asteroid.type][2] < Game.USER.x + 47.5 < asteroid.x + aHit[asteroid.type][2] + aHit[asteroid.type][0]:
                if asteroid.y + aHit[asteroid.type][3] < Game.USER.y + 2.5 < asteroid.y + aHit[asteroid.type][3] + aHit[asteroid.type][1] or asteroid.y + aHit[asteroid.type][3] < Game.USER.y + 75 < asteroid.y + aHit[asteroid.type][3] + aHit[asteroid.type][1]:
                    Game.handleUserDeath()
                    Game.CURRENT_STATE = globals.HOME_STATE
        clock.tick(100)

pygame.quit()


def main():
    print("hello")
    return 0

if __name__ == '__main__':
    main()