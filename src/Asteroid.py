import globals
import pygame
import random

class Asteroid:
    def __init__(self, y = 0):
        self.x = random.randint(-20, globals.GAME_WINDOW_WIDTH - 20)
        self.y = y
        self.type = random.randint(0,6)
        self.vel = random.randint(1,3) * 3
    def draw(self, win):
        win.blit(globals.ASTEROID_IMAGES[self.type], (self.x, self.y))
        #pygame.draw.ellipse(win, (0, 255, 0), (self.x + aHit[self.chose][2], self.y + aHit[self.chose][3], aHit[self.chose][0], aHit[self.chose][1]), 2)
