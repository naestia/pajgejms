import pygame
from config import *
from sprites import *

# ---- CLASSES ----


# ---- LIST OF VARIABLES ----
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Random vars
size = (255, 255)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Calibri", 25, True, False)
clock = pygame.time.Clock()
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10
width = 20
height = 20
margin = 5
count = 0

# ---- Naming the game ----
pygame.display.set_caption("Collarbone")
player_UP = pygame.image.load("player/BACK_UP.png")
player_RIGHT = pygame.image.load("player/RIGHT_RIGHT.png")
player_LEFT = pygame.image.load("player/LEFT_LEFT.png")
player_DOWN = pygame.image.load("player/FRONT_DOWN.png")
sprite = player_DOWN

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -3
                sprite = player_LEFT
            elif event.key == pygame.K_d:
                x_speed = 3
                sprite = player_RIGHT
            elif event.key == pygame.K_w:
                y_speed = -3
                sprite = player_UP
            elif event.key == pygame.K_s:
                y_speed = 3
                sprite = player_DOWN
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0

    x_coord += x_speed
    y_coord += y_speed

    screen.fill(BLACK)
    # ---- Draw here ----
    screen.blit(sprite, (x_coord, y_coord))
    # draw_stick_figure(screen, x_coord, y_coord)

    # ---- Draw here ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
