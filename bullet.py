import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        super().__init__()
        self.image = pygame.Surface((30,5))
        self.rect = self.image.get_rect(center = position)
        self.image.fill('brown')
        self.direction = direction

    def bullet_move(self):
        self.rect.x += 10 * self.direction

    def destroy(self):
        if self.rect.x <= -500 or self.rect.x >= 2000:
            self.kill()

    def update(self):
        self.bullet_move()
        self.destroy()
