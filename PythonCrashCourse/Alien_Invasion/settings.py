
class Settings:

    def __init__(self):
        
        self.fleet_drop_speed = 10
        # the number that will choose direction
        

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 70)
        self.not_started = True
        self.preview_bg_color = (0, 0, 0)

        # ship settings
        self.ship_limit = 5

        # bullet settings
        
        self.bullet_height = 25
        self.bullet_color = (255, 255, 0)

        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

        self.difficulty_chosen = False

    def initialize_dynamic_settings(self):
        self.ship_speed = 4.0
        self.bullet_speed = 5.0
        self.alien_speed = 2.
        self.bullets_allowed = 5

        self.bullet_width = 5

        self.alien_direction = 1

    def hard_buff(self):
        self.ship_speed = 5.0
        self.bullet_speed = 2.5
        self.alien_speed = 4.
        self.bullets_allowed = 3

    def cheat_buff(self):
        self.ship_speed = 10.
        self.bullet_width = 100
        self.bullet_speed = 10.
        self.bullets_allowed = 100

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


        