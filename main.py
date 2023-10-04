import pygame
import sys
from level import *

pygame.init()

screen_w, screen_h = 1200, 600
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()

levelbase = LevelBase(screen, level_date)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill('black')
    levelbase.update()

    pygame.display.update()
    clock.tick(60)