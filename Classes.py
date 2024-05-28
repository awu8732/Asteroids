import pygame
import random




asteroids = [pygame.image.load('Pictures/Asteroid11.png'), pygame.image.load('Pictures/Asteroid12.png'),
             pygame.image.load('Pictures/Asteroid21.png'), pygame.image.load('Pictures/Asteroid22.png'),
             pygame.image.load('Pictures/Asteroid31.png'), pygame.image.load('Pictures/Asteroid32.png'),
             pygame.image.load('Pictures/Asteroid42.png')]
coin = pygame.image.load('Pictures/coin.png')
ship = pygame.image.load('Pictures/fighter.png')
explosion = pygame.image.load('Pictures/explosion.jpg')

aHit = {0: [67, 88, 13, 3], 1: [48, 62, 9, 2], 2: [81, 81, 9, 6], 3: [49, 49, 4, 6],
        4: [81, 105, 0, 0], 5: [40, 53, 0, 0], 6: [49, 40, 24, 9]}

class Button:
    def __init__(self, color, x, y, width, height, text = '', textsize = 60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textsize = textsize
    def draw (self, win , outline = None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.textsize)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isPressed(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Asteroid:
    def __init__(self, y = 0):
        self.x = random.randint(-20, 980)
        self.y = y
        self.chose = random.randint(0,6)
        self.vel = random.randint(1,3) * 3
    def draw(self, win):
        win.blit(asteroids[self.chose], (self.x, self.y))
        #pygame.draw.ellipse(win, (0, 255, 0), (self.x + aHit[self.chose][2], self.y + aHit[self.chose][3], aHit[self.chose][0], aHit[self.chose][1]), 2)

class Coin:
    def __init__(self, y = 0):
        self.x = random.randint(-20, 980)
        self.y = y
        self.vel = random.randint(5, 15)
    def draw(self, win):
        win.blit(coin, (self.x, self.y))
        #pygame.draw.rect(win, (0, 255, 0), (self.x + 7.5, self.y + 7.5, 18, 18), 2)

class Lasers:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 30
    def draw(self, win):
        pygame.draw.line(win, (255, 0, 0), (self.x, self.y), (self.x, self.y + 18), 3)

class Ship:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.hitbox = ((20, 72.5), (75, 18))
        self.magsize = 20
    def draw(self, win):
        win.blit(ship, (self.x, self.y))
        #pygame.draw.rect(win, (0, 255, 0), (self.x, self.y + 59.5, 75, 15.5), 1)
        #pygame.draw.rect(win, (0, 255, 0), (self.x + 27.5, self.y + 2.5, 20, 72.5), 1)
    def hitbox(self, x, y):
        pass


