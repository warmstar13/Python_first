import pygame

from pathlib import Path

class Star:
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.rect_screen = ai_game.screen.get_rect()
        self.path = Path(__file__).parent / "images/star-face-transparent.png"
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.rect_screen.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)