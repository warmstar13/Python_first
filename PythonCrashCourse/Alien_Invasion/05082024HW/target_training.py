import pygame
from archer import Archer
import sys

class TargetTraining:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.archer = Archer(self)

    def start(self):
        while True:
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((30, 128, 0))
        self.archer.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = TargetTraining()
    game.start()