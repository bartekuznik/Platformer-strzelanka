import pygame
import sys

pygame.init()

screen_w, screen_h = 1200, 600
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill('black')
    clock.tick(60)