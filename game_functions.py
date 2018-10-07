import sys, pygame

from bullet import Bullet

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Обработка нажатия клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Обработка отпускания клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets):
    """Обработка нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(game_settings, screen, ship, bullets):
    """Обновление изображения на экране и отображение нового экрана"""
    screen.fill(game_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули"""
    bullets.update()
    # Удаление пуль, вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достигнут"""
    # Cоздание пули и включение ее в группу bullets
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)