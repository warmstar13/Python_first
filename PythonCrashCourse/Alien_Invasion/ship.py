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

    def blitme(self):
        self.screen.blit(self.image, self.rect)