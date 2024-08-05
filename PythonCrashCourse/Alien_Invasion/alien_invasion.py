import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from star import Star
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
# from random import randint

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.game_active = False

        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_height = self.screen.get_height()
        self.settings.screen_width = self.screen.get_width()
        self.play_button = Button(self, "Play")

        self.stats = GameStats(self)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.star = Star(self)
        pygame.display.set_caption("Alien Invasion")
        self._create_fleet()
 
    def run_game(self):
        """Start the main loop for the game."""
        # while self.settings.not_started:
        #     self.screen.fill(self.settings.preview_bg_color)
        #     self.star.blitme()
        #     pygame.display.flip()
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             self.settings.not_started = False

        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60) 

    def _create_fleet(self):
        # make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        cur_x = alien_width
        cur_y = alien_height
        while cur_y < (self.settings.screen_height - 4 * alien_height):
            while cur_x < (self.settings.screen_width - 2 * alien_width):
                # rand_x = randint(-100, 100)
                # rand_y = randint(-100, 100)
                self._create_alien(cur_x, cur_y)
                cur_x += 2 * alien_width
            cur_y += 2 * alien_height
            cur_x = alien_width

    def _check_fleet_direction(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_direction *= -1

    def _create_alien(self, cur_x, cur_y):
        new_alien = Alien(self)
        new_alien.x = cur_x
        new_alien.rect.x = cur_x
        new_alien.rect.y = cur_y
        self.aliens.add(new_alien)

    def _check_events(self):
     # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.game_active = True
            pygame.mouse.set_visible(False)

            self.bullets.empty()
            self.aliens.empty()

            self.ship.center_ship()
            self._create_fleet()

    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_UP:
            self.ship.move_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.stats.reset_stats()
            self.game_active = True
            pygame.mouse.set_visible(False)

            self.bullets.empty()
            self.aliens.empty()

            self.ship.center_ship()
            self._create_fleet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_UP:
            self.ship.move_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_bottom = False

    def _update_bullets(self):
        # Updating the position of bullets
        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        # Happens, when ship loses health
        if self.stats.ships_left > 0: 
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()    
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_direction()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()

    def _update_screen(self):

        # Make the most recently drawn screen visible.
        self.screen.fill(self.settings.bg_color)
        self.aliens.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
            