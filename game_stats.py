class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_status()
        #start alien invasion in an active state
        self.game_activate = False
    
    def reset_status(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0 