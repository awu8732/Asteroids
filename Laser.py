import pygame

class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 30
    def draw(self, win):
        pygame.draw.line(win, (255, 0, 0), (self.x, self.y), (self.x, self.y + 18), 3)