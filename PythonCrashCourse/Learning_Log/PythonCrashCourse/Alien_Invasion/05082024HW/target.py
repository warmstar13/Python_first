import pygame

class Target:

    def __init__(self, arc):
        self.screen = arc.screen
        self.screen_rect = self.screen.get_rect()

        self.upper_point = 50
        self.lower_point = self.screen_rect.height - 150
        self.y = 50
        self.coef = -2
        self.rect = pygame.Rect(self.screen_rect.width - 150, self.y, 100, 100)
        self.color = (10, 230, 10)
        self.addspeed = 1

    def change_pos(self):
        if self.y <= self.upper_point or self.y >= self.lower_point:
            self.coef *= -1
        self.y += self.coef * self.addspeed

    def blitme(self):
        self.rect = pygame.Rect(self.screen_rect.width - 150, self.y, 100, 100)
        pygame.draw.rect(self.screen, self.color, self.rect)