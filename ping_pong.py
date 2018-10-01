"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame
from pygame.sprite import Group
from left_paddle import LeftPaddle
from right_paddle import RightPaddle
from ai_horizontal_paddle import HorizontalPaddle
from player_horizontal_paddle import PlayerHorizontalPaddle
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    """Main game setup"""
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ping Pong")
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play", stats)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ball group
    balls = Group()
    # Make paddle objects
    left_paddle = LeftPaddle(ai_settings, screen)
    right_paddle = RightPaddle(ai_settings, screen)
    horizontal_paddle = HorizontalPaddle(ai_settings, screen)
    player_horizontal_paddle = PlayerHorizontalPaddle(ai_settings, screen)
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, left_paddle, player_horizontal_paddle, balls)
        if stats.game_active:
            left_paddle.update(ai_settings)
            player_horizontal_paddle.update(ai_settings)
            right_paddle.update(ai_settings)
            horizontal_paddle.update(ai_settings)
            gf.update_balls(ai_settings, stats, screen, sb, left_paddle, player_horizontal_paddle, right_paddle,
                            horizontal_paddle, balls, play_button)
            gf.update_right_paddle(ai_settings, right_paddle)
            gf.update_horizontal_paddle(ai_settings, horizontal_paddle)
        gf.update_screen(ai_settings, screen, stats, sb, left_paddle, player_horizontal_paddle, right_paddle,
                         horizontal_paddle, balls, play_button)


run_game()
