import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    def __init__(self, arc):
        super().__init__()
        self.screen = arc.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 30, 10)
        self.rect.midleft = arc.archer.rect.midright

        self.color = (200, 200, 30)

    def update(self):
        self.rect.x += 10
    
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)