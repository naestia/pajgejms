import pygame
from config import *
from sprites import *
import sys
from pytmx.util_pygame import load_pygame


# ---- CLASSES ----
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet('player/sprites_allsides.png')
        self.terrain_spritesheet = Spritesheet('terrain/terrain.png')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Grass(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == 'P':
                    Player(self, j, i)

    def blit_all_tiles(self, screen, tmxdata, world_offset):
        """for layer in tmxdata:
            for tile in layer.tiles():
                self.x_p = tile[0] * TILESIZE + world_offset[0]
                self.y_p = tile[1] * TILESIZE + world_offset[1]
                screen.blit(tile[2], (self.x_p, self.y_p))"""
        pass

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(60)
        pygame.display.update()

    def main(self):
        # Game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
