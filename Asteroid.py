import pygame
import random

asteroidImages = [pygame.image.load('Pictures/Asteroid11.png'), pygame.image.load('Pictures/Asteroid12.png'),
             pygame.image.load('Pictures/Asteroid21.png'), pygame.image.load('Pictures/Asteroid22.png'),
             pygame.image.load('Pictures/Asteroid31.png'), pygame.image.load('Pictures/Asteroid32.png'),
             pygame.image.load('Pictures/Asteroid42.png')]

class Asteroid:
    def __init__(self, y = 0):
        self.x = random.randint(-20, 980)
        self.y = y
        self.chose = random.randint(0,6)
        self.vel = random.randint(1,3) * 3
    def draw(self, win):
        win.blit(asteroidImages[self.chose], (self.x, self.y))
        #pygame.draw.ellipse(win, (0, 255, 0), (self.x + aHit[self.chose][2], self.y + aHit[self.chose][3], aHit[self.chose][0], aHit[self.chose][1]), 2)
