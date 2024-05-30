import globals
import pygame
import time

from Button import Button

def initializeGame():
    pygame.init()
    pygame.display.set_caption("Asteroids")

    initializeGameVariables()
    initializeGameObjects()

def initializeGameObjects():
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
    return 

def initializeGameVariables():
    global CURRENT_STATE
    CURRENT_STATE = globals.HOME_STATE

def pauseScreen(interval = 2):
    goal = time.time() + interval
    while (time.time() < goal):
        pass

initializeGame()

