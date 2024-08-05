import pygame

class Archer:
    def __init__(self, arc):
        self.screen = arc.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 100, 20)

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)