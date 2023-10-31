import pygame


class End(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((30,60))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('yellow')
        