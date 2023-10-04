import pygame
from pygame.sprite import AbstractGroup 

class Block(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('red')