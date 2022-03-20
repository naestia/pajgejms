import pygame
import math
from math import pi
import funcs


# ---- PLAYER SKETCH ----
def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, (0, 0, 0), [1+x, y, 10, 10], 0)

    pygame.draw.line(screen, (0, 0, 0), [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, (0, 0, 0), [5 + x, 17 + y], [x, 27 + y], 2)

    pygame.draw.line(screen, (255, 0, 0), [5 + x, 17 + y], [5 + x, 7 + y], 2)

    pygame.draw.line(screen, (255, 0, 0), [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, (255, 0, 0), [5 + x, 7 + y], [1 + x, 17 + y], 2)


# ---- INITIATION OF GAME ----
pygame.init()

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
player_image = pygame.image.load("among_us.png")
player_image = pygame.transform.scale(player_image, ((587//10), (744//10)))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    # ---- Draw here ----
    for column in range(10):
        pygame.draw.rect(screen, WHITE, [count, 0, width, height])
        count += 20
    # draw_stick_figure(screen, x_coord, y_coord)

    # ---- Draw here ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
