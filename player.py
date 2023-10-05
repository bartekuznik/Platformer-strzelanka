import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((20,40))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('blue')
        self.gravity = 0
        self.jump_value = -40

    def add_gravity(self):
        self.gravity += 3
        self.rect.y += self.gravity

    def jump(self):
        self.gravity = self.jump_value

    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 7
        if keys[pygame.K_RIGHT]:
            self.rect.x += 7
        if keys[pygame.K_SPACE]:
            self.jump()

    def update(self):
        self.add_gravity()
        self.moving()