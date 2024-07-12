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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.star = Star(self)
        pygame.display.set_caption("Alien Invasion")
 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60) 

    def _check_events(self):
     # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Make the most recently drawn screen visible.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.star.blitme()
        pygame.display.flip()

        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()