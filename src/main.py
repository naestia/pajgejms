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
size = (1200, 700)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Calibri", 25, True, False)
clock = pygame.time.Clock()
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10


# ---- Naming the game ----
pygame.display.set_caption("Collarbone")
player_image = pygame.image.load("among_us.png")
player_image = pygame.transform.scale(player_image, ((587//10), (744//10)))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -3
            elif event.key == pygame.K_d:
                x_speed = 3
            elif event.key == pygame.K_w:
                y_speed = -3
            elif event.key == pygame.K_s:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0

    x_coord += x_speed
    y_coord += y_speed

    screen.fill(WHITE)
    # ---- Draw here ----

    screen.blit(player_image, [x_coord, y_coord])
    # draw_stick_figure(screen, x_coord, y_coord)

    # ---- Draw here ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
