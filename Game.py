import globals
import pygame
import time

from Button import Button
from Player import Player

#=============================================================================================
#==================================== GAME INITIALIZATION ====================================
#=============================================================================================

def initializeGame():
    pygame.init()
    pygame.display.set_caption("Asteroids")

    initializeGameVariables()
    initializeGameElements()

def initializeGameElements():
    """BUTTONS"""
    global PLAY_BUTTON, STORE_BUTTON, BACK_BUTTON
    PLAY_BUTTON = Button((0, 191, 255), 400, 300, 200, 100, "PLAY")
    STORE_BUTTON = Button((0, 191, 255), 400, 415, 200, 100, "STORE")
    BACK_BUTTON = Button((0, 191, 255), 20, 20, 100, 50, "Back")

    """ONSCREEN GAME ELEMENTS"""
    global ONSCREEN_ASTEROIDS, ONSCREEN_COINS, ONSCREEN_LASERS
    ONSCREEN_ASTEROIDS = []
    ONSCREEN_COINS = []
    ONSCREEN_LASERS = []

    global USER
    USER = Player(400, 250, 6)
    return 

def initializeGameVariables():
    global CURRENT_STATE
    CURRENT_STATE = globals.HOME_STATE

    global WIN
    WIN = pygame.display.set_mode((globals.GAME_WINDOW_LENGTH, globals.GAME_WINDOW_WIDTH))

#=============================================================================================
#======================================= GAME FUNCTIONS ======================================
#=============================================================================================

def handleUserDeath():
    if globals.CURRENT_SCORE > globals.CURRENT_BEST_SCORE:
        globals.CURRENT_BEST_SCORE = globals.CURRENT_SCORE
    resetGameState()

    #delete later
    DEATH_TEXT = globals.LARGE_FONT.render('YOU DIED!', 1, (200, 0, 0))

    WIN.blit(DEATH_TEXT, (300, 300))
    pygame.display.update()
    pauseScreen()


def resetGameState():
    globals.CURRENT_SCORE = 0
    ONSCREEN_ASTEROIDS.clear()
    ONSCREEN_COINS.clear()
    ONSCREEN_LASERS.clear()
    USER.x = 400
    USER.y = 250
    USER.ammo = 0

def updateOnscreenUIElements():
    updateOnscreenLasers()
    updateOnscreenCoins()
    updateOnscreenAsteroids()
    return
def updateOnscreenLasers():
    for i in range(len(ONSCREEN_LASERS)):
        if i >= len(ONSCREEN_LASERS):
            continue
        currentLaser = ONSCREEN_LASERS[i]
        if (currentLaser.y > 0):
            currentLaser.y -= USER.bulletSpeed
        else:
            ONSCREEN_LASERS.pop(i)
def updateOnscreenCoins():
    for i in range(len(ONSCREEN_COINS)):
        if i >= len(ONSCREEN_COINS):
            continue
        currentCoin = ONSCREEN_COINS[i]
        if (currentCoin.y < globals.GAME_WINDOW_WIDTH):
            currentCoin.y += currentCoin.vel
        else:
            ONSCREEN_COINS.pop(i)
def updateOnscreenAsteroids():
    for i in range(len(ONSCREEN_ASTEROIDS)):
        if i >= len(ONSCREEN_ASTEROIDS):
            continue
        currentAsteroid = ONSCREEN_ASTEROIDS[i]
        if (currentAsteroid.y < globals.GAME_WINDOW_WIDTH):
            currentAsteroid.y += currentAsteroid.vel
        else:
            ONSCREEN_ASTEROIDS.pop(i)

#=============================================================================================
#======================================== GAME HELPERS =======================================
#=============================================================================================

def getAmmoBarColor():
    if USER.ammo/USER.maxAmmo >= .75:
        return (0, 255, 0)
    elif USER.ammo/USER.maxAmmo >= .54:
        return (173, 255, 47)
    elif USER.ammo/USER.maxAmmo >= .33:
        return (255, 215, 0)
    else:
        return (255, 0, 0)

def pauseScreen(interval = 2):
    goal = time.time() + interval
    while (time.time() < goal):
        pass

initializeGame()

