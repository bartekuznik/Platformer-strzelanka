import pygame
import sys
from level import *
from level_chunks import *

pygame.init()

screen_w, screen_h = 1200, 600
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()

levelbase = LevelBase(screen, level_date_tabel)

start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start == False:
                start = True

    if start:
        screen.fill('black')
        levelbase.update()

    else:
        screen.fill('black')
        text_font = pygame.font.Font('font/font.ttf', 50)
        top_text = text_font.render('Press "START" to start game',False,'blue')
        top_text_rect = top_text.get_rect(center = (600, 300))
        screen.blit(top_text, top_text_rect)

    pygame.display.update()
    clock.tick(60)