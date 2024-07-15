
class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 70)
        self.not_started = True
        self.preview_bg_color = (0, 0, 0)

        # ship settings
        self.ship_speed = 5.0

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3