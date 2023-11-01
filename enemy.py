import pygame

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((30,60))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('green')

    def movement(self):
        pass

    def update(self, enemies):
        for enemy in enemies:
            enemy.movement()

class HorizntalEnemy(BaseEnemy):
    def __init__(self, position):
        super().__init__(position)
        self.movement_range = 120
        self.x_movement_value = 5

    def movement(self):
        if self.movement_range != 0:
            self.rect.x += self.x_movement_value
            self.movement_range -= 5

        else:
            self.movement_range = 120
            self.x_movement_value *= -1