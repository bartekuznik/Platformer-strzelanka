import pygame
from block import *
from player import *

level_date = [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "g", "g", "g", "g", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "g", "g", "g", "g", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "g", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "g", "g", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "d", "w", "w", "w", "w", "g", "g", "g", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "w", "w", "g", "g", "g", "g", "g", "g", "g", "g"],
         ]
block_size = 60

class LevelBase():
    def __init__(self, screen, level_date):
        self.screen = screen
        self.level_date = level_date
        self.setup_level(self.level_date)

    def setup_level(self, level_date):
        self.blocks = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(level_date):
            for cell_index, cell in enumerate(row):
                x = cell_index * block_size
                y = row_index * block_size
                if cell == "g":
                    block = Block( block_size, (x,y))
                    self.blocks.add(block)
                if cell == "d":
                    self.player = Player((x,y))
                    self.player_group.add(self.player)
                    
        
    def update(self):
        self.blocks.draw(self.screen)
        self.player_group.draw(self.screen)
        self.player.update()

