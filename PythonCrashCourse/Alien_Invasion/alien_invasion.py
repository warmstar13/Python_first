import sys
import pygame
from settings import Settings
from ship import Ship
from star import Star

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_height()
        self.settings.screen_width = self.screen.get_width()

        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        
        # self.star = Star(self)
        pygame.display.set_caption("Alien Invasion")
 
    def run_game(self):
        """Start the main loop for the game."""
        while self.settings.not_started:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.settings.not_started = False
    
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60) 

    def _check_events(self):
     # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_UP:
            self.ship.move_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_UP:
            self.ship.move_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_bottom = False


    def _update_screen(self):
        # Make the most recently drawn screen visible.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # self.star.blitme()
        pygame.display.flip()

        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
            