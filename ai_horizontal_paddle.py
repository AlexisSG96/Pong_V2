"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame
from pygame.sprite import Sprite


class HorizontalPaddle(Sprite):
    def __init__(self, ai_settings, screen):
        """Create the Right_Paddle and set its starting position."""
        super(HorizontalPaddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.top_rect = pygame.Rect(0, 0, ai_settings.horizontal_paddle_width, ai_settings.horizontal_paddle_height)
        self.bot_rect = pygame.Rect(0, 0, ai_settings.horizontal_paddle_width, ai_settings.horizontal_paddle_height)
        self.screen_rect = screen.get_rect()
        self.color = ai_settings.horizontal_paddle_color
        self.height = float(ai_settings.horizontal_paddle_height)
        # Paddle starts at the bottom and top
        self.top_rect.centerx = self.screen_rect.centerx + (self.screen_rect.centerx/2)
        self.top_rect.top = self.screen_rect.top
        self.bot_rect.centerx = self.screen_rect.centerx + (self.screen_rect.centerx/2)
        self.bot_rect.bottom = self.screen_rect.bottom
        # Store a decimal value for the ship's center.
        self.x = float(self.top_rect.x)
        self.x = float(self.bot_rect.x)
        # Movement flag for continuous movement
        self.moving_left = False
        self.moving_right = False
        self.center = ai_settings.screen_center

    def update(self, ai_settings):
        """Update the paddles position based on the movement flag."""
        if ai_settings.screen_width - ai_settings.screen_width/6 > ai_settings.ball_x_position > \
                ai_settings.screen_center:
            self.x = ai_settings.ball_x_position * ai_settings.horizontal_paddle_speed_factor
        self.top_rect.x = self.x
        if self.moving_right and self.top_rect.right < ai_settings.screen_width:
            self.center += self.ai_settings.horizontal_paddle_speed_factor
        if self.moving_left and self.top_rect.left > ai_settings.screen_center:
            self.center -= self.ai_settings.horizontal_paddle_speed_factor
        self.bot_rect.x = self.x
        if self.moving_right and self.bot_rect.right < ai_settings.screen_width:
            self.center += self.ai_settings.horizontal_paddle_speed_factor
        if self.moving_left and self.bot_rect.left > ai_settings.screen_center:
            self.center -= self.ai_settings.horizontal_paddle_speed_factor

    def check_edges(self, ai_settings):
        """Check if paddle hits an edge"""
        if self.top_rect.right >= ai_settings.screen_width:
            return True
        elif self.top_rect.left <= ai_settings.screen_center:
            return True
        if self.bot_rect.right >= ai_settings.screen_width:
            return True
        elif self.bot_rect.left <= ai_settings.screen_center:
            return True

    def center_horizontal_paddle(self):
        """Center the paddle on the screen to the right of center of screen."""
        self.x = self.center
        self.top_rect.x = self.x
        self.bot_rect.x = self.x

    def draw_horizontal_paddle(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.top_rect)
        pygame.draw.rect(self.screen, self.color, self.bot_rect)
