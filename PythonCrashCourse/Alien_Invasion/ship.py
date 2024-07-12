import pygame

from pathlib import Path

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.rect_screen = ai_game.screen.get_rect()
        self.path = Path(__file__).parent / "images/hand-drawn-spaceship-background.bmp"
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (180, 200))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.rect_screen.midbottom

        # Setting the moving of the ship

        self.move_right = False
        self.move_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_left:
            self.rect.x -= 1
        elif self.move_right:
            self.rect.x += 1