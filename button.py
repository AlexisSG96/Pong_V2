"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg, stats):
        """Play Button and screen"""
        self.stats = stats
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimension and properties of the button
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Start Screen settings
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.red_2 = (255, 50, 50)
        self.brit_font = pygame.font.SysFont("Britannic Bold", 250)
        self.brit_font_2 = pygame.font.SysFont("Britannic Bold", 100)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prep Start Screen
        self.start_label = self.brit_font.render("PONG:", True, self.green)
        self.start_center_x = ai_settings.screen_width/4
        self.start_center_y = ai_settings.screen_height/6
        self.start_rect = pygame.Rect(self.start_center_x, self.start_center_y, 0, 0)
        # Description Screen
        self.des_label = self.brit_font_2.render("AI -- NO WALLS", True, self.red)
        self.des_center_x = ai_settings.screen_width/3 - 20
        self.des_center_y = ai_settings.screen_height/3 + 20
        self.des_rect = pygame.Rect(self.des_center_x, self.des_center_y, 0, 0)
        # Match Point
        self.match_label = self.font.render("Match Point: " + str(stats.score_goal), True, self.red_2)
        self.match_center_x = ai_settings.screen_width/3 + 88
        self.match_center_y = ai_settings.screen_height/2 + 40
        self.match_rect = pygame.Rect(self.match_center_x, self.match_center_y, 0, 0)

        # The button message needs to be prepped only once.
        self.msg_image = None
        self.msg_image_rect = None

        self.winner_rect = pygame.Rect(0, 0, self.width, self.height)
        self.winner_rect.center = self.screen_rect.center
        self.winner_image = None
        self.winner_image_rect = None
        self.count = 0

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.black)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def end_screen(self, stats):
        self.winner_image = self.brit_font_2.render("Winner: " + str(stats.winner), True, self.red)
        self.winner_image_rect = self.winner_image.get_rect()
        self.winner_image_rect.center = self.rect.center
        while self.count < 1000:
            self.screen.fill(self.black)
            self.screen.blit(self.winner_image, self.winner_image_rect)
            pygame.display.flip()
            self.count += 1
        stats.game_active = False
        pygame.mouse.set_visible(True)
        self.count = 0

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.black)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.start_label, self.start_rect)
        self.screen.blit(self.des_label, self.des_rect)
        self.screen.blit(self.match_label, self.match_rect)
