import pygame
from archer import Archer
from target import Target
from arrow import Arrow
import sys

class TargetTraining:

    def __init__(self):
        pygame.init()

        self.game_active = True

        self.screen = pygame.display.set_mode((1200, 800))
        self.archer = Archer(self)
        self.target = Target(self)
        self.arrows = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.limit = 3
        self.throwed = 0

    def start(self):
        while True:
            self._check_events()

            if self.game_active:
                self._change_positions()
            
            self._update_screen()
            self.clock.tick(60)
            
    def _change_positions(self):
        if self.archer.up:
            self.archer.y -= 3
        if self.archer.down:
            self.archer.y += 3
        self.target.change_pos()
        self.arrows.update()
        self._check_collisions()

    def _check_collisions(self):
        col_spr = pygame.sprite.spritecollideany(self.target, self.arrows)
        if col_spr:
            self.game_active = False
            
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.archer.down = True
                elif event.key == pygame.K_w:
                    self.archer.up = True
                elif event.key == pygame.K_SPACE:
                    self._fire_arrow()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.archer.down = False
                elif event.key == pygame.K_w:
                    self.archer.up = False

    def _fire_arrow(self):
        if (self.limit > self.throwed):
            newarr = Arrow(self)
            self.arrows.add(newarr)
            self.throwed += 1


    def _update_screen(self):
        self.screen.fill((30, 128, 0))
        self.archer.blitme()
        self.target.blitme()
        for arr in self.arrows.sprites():
            arr.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = TargetTraining()
    game.start()