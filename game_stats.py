"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""


class GameStats:
    """Track statistics for Pong."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        self.player_score = 0
        self.cpu_score = 0
        # High score should never be reset.
        self.high_score = 0
        self.score_goal = 7
        self.left_paddle_left = None
        self.winner = "None"

    def reset_stats(self):
        self.player_score = 0
        self.cpu_score = 0
