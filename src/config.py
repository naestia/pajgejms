import pygame.image
from pytmx.util_pygame import load_pygame

WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32

# ----COLORS----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ----PLAYER----
PLAYER_LAYER = 3
PLAYER_SPEED = 3

BLOCK_LAYER = 2
GROUND_LAYER = 1
tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B........P.........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]

# ----MAP----
#tmxdata = load_pygame("terrain/chess.tmx")