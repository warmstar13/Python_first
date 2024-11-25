
class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 150)
        self.not_started = True

        # ship settings
        self.ship_speed = 5.0

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3