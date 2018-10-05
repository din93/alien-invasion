import pygame

from settings import Settings
from ship import Ship
import game_functions

def run_game():
    # Инициализация pygame, settings и создание объекта экрана
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля
    ship = Ship(screen)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        game_functions.check_events()
        # Перерисовка экрана
        game_functions.update_screen(game_settings, screen, ship)     


if __name__=='__main__':
    run_game()