import pygame
from pygame.sprite import Sprite
from pathlib import Path
class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.path = Path(__file__).parent / "images/alien-transparent.png"
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
