import pygame
from archer import Archer
from target import Target
from arrow import Arrow
from button import Button
import sys

class TargetTraining:

    def __init__(self):
        pygame.init()

        self.game_active = False

        self.screen = pygame.display.set_mode((1200, 800))
        self.archer = Archer(self)
        self.target = Target(self)
        self.button = Button(self, "Play")
        self.arrows = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.limit = 3
        self.throwed = 0
        self.lost = 0

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
        for arr in self.arrows.copy():
            if arr.rect.x > self.screen.get_width():
                self.arrows.remove(arr)
                self.lost += 1
        self._check_collisions()
        if self.lost == self.limit:
            self.game_active = False

    def _check_collisions(self):
        col_spr = pygame.sprite.spritecollideany(self.target, self.arrows)
        if col_spr:
            self._reset()
            self.target.addspeed += 1
            
            

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_active == False:
                    cur_pos = pygame.mouse.get_pos()
                    if self.button.rect.collidepoint(cur_pos):
                        self.game_active = True
                        self._reset()

    def _reset(self):
        self.arrows.empty()
        self.throwed = 0
        self.lost = 0
        self.target.y = 50
        self.target.coef = -2
        self.archer.y = 400

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
        if not self.game_active:
            self.button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    game = TargetTraining()
    game.start()