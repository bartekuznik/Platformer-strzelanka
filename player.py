import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((20,60))
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill('blue')
        self.gravity = 0
        self.jump_value = -15
        self.moving_right = False
        self.moving_left = False
        self.onGround = True
        self.y_momentum = 0
        self.player_move = [0, 0]

    def add_gravity(self):
        """ if self.y_momentum < 1:
            self.y_momentum += 0.2
        else:
            self.y_momentum = 1
        self.player_move[1] = self.y_momentum"""
    
        self.player_move[1] += self.y_momentum
        self.y_momentum += 0.5
        if self.y_momentum > 10:
            self.y_momentum = 10

    def jump(self):
        self.y_momentum = self.jump_value

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving_left = True
            self.moving_right = False
        elif keys[pygame.K_RIGHT]:
            self.moving_right = True
            self.moving_left = False
        else:
            self.moving_right = False
            self.moving_left = False

        if keys[pygame.K_SPACE] and self.onGround == True:
            self.jump()
            self.onGround = False
            #print(self.player_move[1])


    def moving(self):
        self.player_move = [0, 0]
        
        if self.rect.left <= 300 or self.rect.right >= 900:
            if self.moving_right == True:
                self.player_move[0] += 7
            if self.moving_left == True:
                self.player_move[0] -= 7

        #print(self.player_move)

    """def test_fuction(self):
        if self.player_move[1] > 600 - self.image.get_height(): # 600 - wyskość okna
            self.y_momentum = - self.y_momentum
        else:
            self.y_momentum += 0.2
        self.player_move[1] += self.y_momentum"""

    def update(self):
        self.player_input()
        self.moving()
        #self.add_gravity()
        #self.test_fuction()
        #print(self.rect.y,self.rect.x)