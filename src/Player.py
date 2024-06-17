import globals
import pygame

class Player:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.speed = vel
        self.hitbox = ((20, 72.5), (75, 18))
        self.maxAmmo = 20
        self.ammo = self.maxAmmo
        self.bulletSpeed = 36
    def draw(self, win):
        win.blit(globals.FIGHTER_IMAGE, (self.x, self.y))
        #pygame.draw.rect(win, (0, 255, 0), (self.x, self.y + 59.5, 75, 15.5), 1)
        #pygame.draw.rect(win, (0, 255, 0), (self.x + 27.5, self.y + 2.5, 20, 72.5), 1)
    def hitbox(self, x, y):
        pass