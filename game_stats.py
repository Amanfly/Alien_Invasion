class GameStats():
    """Track  statistics for alien Invasion"""
    def __init__(self,ai_settings):
        """Initialize statistics"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #start alien Invasion in active stats
        self.game_active=False
    def reset_stats(self):
        """Initialize the statistics that can change during game"""
        self.ships_left=self.ai_settings.ship_limit
