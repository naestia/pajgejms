import pygame
import math
from math import pi
from myfunctions.funcs import MyColors, draw_snowman

# ---- INITIATION OF GAME ----
pygame.init()

# ---- LIST OF VARIABLES ----
# Colors
my_colors = MyColors()

# Random vars
size = (700, 500)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Calibri", 25, True, False)
clock = pygame.time.Clock()

# ---- Naming the game ----
pygame.display.set_caption("Collarbone")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(my_colors.BLACK)
    # ---- Draw here ----

    draw_snowman(screen, 10, 10)

    # ---- Draw here ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()