"""
Game frontend module. This module is responsible for rendering the game and handling
user input.
"""
import pygame


class GameFrontend:
    def __init__(self, options):
        self.options = options

        # ------------------------------------------------------------------------------
        # Create the game window and clock
        # ------------------------------------------------------------------------------
        self.window = pygame.display.set_mode((self.options.WIDTH, self.options.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.options.GAME_NAME)

        # ------------------------------------------------------------------------------
        # Create the game assets (images, sounds, etc.)
        # ------------------------------------------------------------------------------
        # rectangles for pieces in order to use the rectangles for movement later
        self.yellow = pygame.Rect(120, 200, self.options.PIECE_WIDTH, self.options.PIECE_HEIGHT)
        self.purple = pygame.Rect(350, 200, self.options.PIECE_WIDTH, self.options.PIECE_HEIGHT)

        # events when hit (events are used to check for during the main loop)
        self.yellow_is_hit = pygame.USEREVENT + 1
        self.purple_is_hit = pygame.USEREVENT + 2

    @staticmethod
    def update_after_change():
        pygame.display.update()

    def run_game(self):
        pass



