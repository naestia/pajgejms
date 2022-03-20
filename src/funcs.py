# Functions to use in main.py
import pygame


class MyColors:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)


myColors = MyColors()


def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, myColors.WHITE, [35 + x, y, 25, 25])
    pygame.draw.ellipse(screen, myColors.WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, myColors.WHITE, [x, 65 + y, 100, 100])



if __name__ == '__main__':
    pass
