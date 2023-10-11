import pygame
from block import *
from player import *

level_date = [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "d", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "g", "g", "g", "g", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w", "g", "g", "g", "g", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "g", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "g", "g", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "w", "w", "w", "w", "w", "g", "g", "g", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
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
                    
    def block_collide(self, blocks):
        block_collision = []
        for block in blocks:
            if self.player.rect.colliderect(block):
                block_collision.append(block)
        return block_collision
    
    def horizontal_collisions(self):
        self.player.rect.x += self.player.player_move[0]
        coll_block = self.block_collide(self.blocks)
        for block in coll_block:
            if self.player.player_move[0] > 0 and self.player.moving_right == True:
                self.player.rect.right = block.rect.left
                print("PRAWO")
            if self.player.player_move[0] < 0 and self.player.moving_left == True:
                self.player.rect.left = block.rect.right
                print("LEWO")
    
    def vertical_collisions(self):
        self.player.add_gravity()
        self.player.rect.y += self.player.player_move[1]
        coll_block = self.block_collide(self.blocks)
        for block in coll_block:
            if self.player.player_move[1] > 0:
                self.player.rect.bottom = block.rect.top
                #self.player.player_move[1] = 0
            if self.player.player_move[1] < 0:
                self.player.rect.top = block.rect.bottom
                
    def update(self):
        self.blocks.draw(self.screen)
        self.player_group.draw(self.screen)
        self.block_collide(self.blocks)
        self.horizontal_collisions()
        self.vertical_collisions()
        self.player.update()

