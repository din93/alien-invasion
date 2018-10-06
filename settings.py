class Settings:
    """Настройки игры Alien Invasion"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Параметры корабля
        self.ship_speed_factor = 1.5
        