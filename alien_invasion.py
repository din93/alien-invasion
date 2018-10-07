import pygame
from pygame.sprite import Group

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
    ship = Ship(game_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        game_functions.check_events(game_settings, screen, ship, bullets)
        # Обновление позиции корабля
        ship.update()
        # Обновление позиций пуль
        game_functions.update_bullets(bullets)
        # Перерисовка экрана
        game_functions.update_screen(game_settings, screen, ship, bullets)     


if __name__=='__main__':
    run_game()