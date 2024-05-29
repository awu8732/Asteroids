import pygame

#===================== GAME VARIABLES =====================
GAME_QUIT = -1
GAME_STATE = 0
HOME_STATE = 1
STORE_STATE = 2

CURRENT_BEST_SCORE = 0
CURRENT_SCORE = 0
CURRENT_COIN_COUNT = 100

ATTRIBUTE_UPGRADE_COSTS = [5, 10, 15, 20, 25]

#===================== IMAGE PATHS =====================
ASTEROID_IMAGE_PATHS = ['Pictures/Asteroid11.png', 'Pictures/Asteroid12.png',
                        'Pictures/Asteroid21.png', 'Pictures/Asteroid12.png', 
                        'Pictures/Asteroid31.png', 'Pictures/Asteroid12.png', 
                        'Pictures/Asteroid42.png']
FIGHTER_IMAGE_PATH = 'Pictures/fighter.png'
LOGO_IMAGE_PATH = 'Pictures/Logo.png'
COIN_IMAGE_PATH = 'Pictures/coin.png'
BACKGROUND_IMAGE_PATH = 'Pictures/space.png'

#===================== INITIALIZE IMAGES =====================
ASTEROID_IMAGES = []
for ASTEROID_PATH in ASTEROID_IMAGE_PATHS:
    ASTEROID_IMAGES.append(pygame.image.load(ASTEROID_PATH))
FIGHTER_IMAGE = pygame.image.load(FIGHTER_IMAGE_PATH)
LOGO_IMAGE = pygame.image.load(LOGO_IMAGE_PATH)
COIN_IMAGE = pygame.image.load(COIN_IMAGE_PATH)
BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_IMAGE_PATH)
