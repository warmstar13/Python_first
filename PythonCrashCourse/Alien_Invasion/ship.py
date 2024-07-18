import pygame

from pathlib import Path

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.rect_screen = ai_game.screen.get_rect()
        
        self.path = Path(__file__).parent / "images/hand-drawn-spaceship-background.bmp"
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (180, 200))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.rect_screen.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Setting the moving of the ship

        self.move_right = False
        self.move_left = False
        self.move_top = False
        self.move_bottom = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.rect.right < self.rect_screen.right:
            self.x += self.settings.ship_speed
        if self.move_top and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.move_bottom and self.rect.bottom < self.rect_screen.bottom:
            self.y += self.settings.ship_speed
        
        self.rect.x = self.x
        self.rect.y = self.y
