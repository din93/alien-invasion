import sys, pygame

from settings import Settings

def run_game():
    # Инициализация pygame, settings и создание объекта экрана
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # При каждом проходе цикла перерисовывается экран
        screen.fill(game_settings.bg_color)
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__=='__main__':
    run_game()