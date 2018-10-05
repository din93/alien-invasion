import sys

import pygame

def check_events():
    """Обработка нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, ship):
    """Обновление изображения на экране и отображение нового экрана"""
    screen.fill(game_settings.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()