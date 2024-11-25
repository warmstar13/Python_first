import pygame

class Archer:
    def __init__(self, arc):
        self.screen = arc.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (255, 0, 0)
        self.y = 400
        self.rect = pygame.Rect(50, 400, 100, 20)

        self.up = False
        self.down = False

    def blitme(self):
        self.rect = pygame.Rect(50, self.y, 100, 20)
        pygame.draw.rect(self.screen, self.color, self.rect)