from pathlib import Path

class GameStats:
    # Tracks statistics

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        path = Path(__file__).parent / "saved_high_score.txt"
        self.high_score = int(path.read_text())
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1