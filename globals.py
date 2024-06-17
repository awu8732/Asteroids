import pygame

#===================== GAME VARIABLES =====================
GAME_WINDOW_LENGTH = 600
GAME_WINDOW_WIDTH = 1000

GAME_QUIT = -1
GAME_STATE = 0
HOME_STATE = 1
STORE_STATE = 2

pygame.font.init()
LARGE_FONT_SIZE = 80
NORMAL_FONT_SIZE = 40
STAT_FONT_SIZE = 30

LARGE_FONT = pygame.font.SysFont('impact', LARGE_FONT_SIZE)
NORMAL_FONT = pygame.font.SysFont(None, NORMAL_FONT_SIZE)
STAT_FONT = pygame.font.SysFont(None, STAT_FONT_SIZE)

CURRENT_BEST_SCORE = 0
CURRENT_SCORE = 0
CURRENT_COIN_COUNT = 100

AMMO_BAR_LENGTH = 20
AMMO_BAR_WIDTH = 100

ATTRIBUTE_UPGRADE_COSTS = [5, 10, 15, 20, 25]

WHITE = (255, 255, 255)
BLACK = (0 ,0 ,0)

# {ATR: [initial, current, increment]}
UPGRADE_ATTRIBUTES = {
    "SPEED": [6, 0, 2],
    "HEALTH": [50, 3, 10],
    "BLASTER SPEED": [6, 2, 3],
    "BLASTER DAMAGE":[15, 0, 10],
    "MAGAZINE CAPACITY": [6, 0, 2],
    "MAGAZINE RELOAD": [10, 0, 5]
}

#===================== IMAGE PATHS =====================
ASTEROID_IMAGE_PATHS = ['assets/Asteroid11.png', 'assets/Asteroid12.png',
                        'assets/Asteroid21.png', 'assets/Asteroid12.png', 
                        'assets/Asteroid31.png', 'assets/Asteroid12.png', 
                        'assets/Asteroid42.png']
FIGHTER_IMAGE_PATH = 'assets/fighter.png'
LOGO_IMAGE_PATH = 'assets/Logo.png'
COIN_IMAGE_PATH = 'assets/coin.png'
BACKGROUND_IMAGE_PATH = 'assets/space.png'

#===================== INITIALIZE IMAGES =====================
ASTEROID_IMAGES = []
for ASTEROID_PATH in ASTEROID_IMAGE_PATHS:
    ASTEROID_IMAGES.append(pygame.image.load(ASTEROID_PATH))
FIGHTER_IMAGE = pygame.image.load(FIGHTER_IMAGE_PATH)
LOGO_IMAGE = pygame.image.load(LOGO_IMAGE_PATH)
COIN_IMAGE = pygame.image.load(COIN_IMAGE_PATH)
BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_IMAGE_PATH)


#get fonts
def check_fonts():
    win = pygame.display.set_mode((GAME_WINDOW_LENGTH, GAME_WINDOW_WIDTH))
    pygame_fonts = pygame.font.get_fonts()

    for i, font in enumerate(pygame_fonts):
        current_font = pygame.font.SysFont(font, 15)
        temp_text = current_font.render(font, 1, (255,0,0))
        win.blit(temp_text, (120 * int(i/30) + 5,20 * (i%30) + 5))

    pygame.display.update()
    
    while 1:
        continue



