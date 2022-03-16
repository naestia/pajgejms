import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    display.fill((0, 0, 0))

    display.blit(player.surf, (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2))

    pygame.display.flip()
    """
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    surf_center = (
            (DISPLAY_WIDTH - surf.get_width()) / 2,
            (DISPLAY_HEIGHT - surf.get_height()) / 2
    )
    display.blit(surf, surf_center)
    pygame.display.flip()
"""