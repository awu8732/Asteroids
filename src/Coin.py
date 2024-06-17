import globals
import pygame
import random

class Coin:
    def __init__(self, y = 0):
        self.x = random.randint(-20, 980)
        self.y = y
        self.vel = random.randint(5, 15)
    def draw(self, win):
        win.blit(globals.COIN_IMAGE, (self.x, self.y))
        #pygame.draw.rect(win, (0, 255, 0), (self.x + 7.5, self.y + 7.5, 18, 18), 2)