"""
Options class that contains all the settings for the game, such as colors, fonts, sounds, images,
and player settings.
"""
import os

import pygame


pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class Options:
    #region Game settings
    FPS = 60
    WIDTH = 900
    HEIGHT = 500
    BORDER = (WIDTH // 2 - 5, 0, 10, HEIGHT)
    MOVEMENT_VELOCITY = 5
    SWING_VELOCITY = 7
    MAX_SWINGS = 3
    #endregion

    #region Colors
    WINDOW_COLOR = (112, 105, 105)

    BLACK_COLOR = (0, 0, 0)
    RED_COLOR = (255, 0, 0)
    GREEN_COLOR = (0, 255, 0)
    #endregion

    #region Text settings
    GAME_NAME = "rpg_heaven"
    HEALTH_FONT = 'comicsans'
    #endregion

    #region Sounds
    SWING_SOUND = pygame.mixer.Sound(os.path.join('assets', 'gun_sound.mp3'))
    TARGET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit_sound.mp3'))
    #endregion

    #region Sound Transformation
    SWING_SOUND.set_volume(0.2)   # lower volume
    #endregion

    #region Images
    YELLOW_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'yellow.png'))
    PURPLE_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'purple.png'))
    BACKGROUND = pygame.image.load(os.path.join('assets', 'space.png'))
    PIECE_WIDTH = 20
    PIECE_HEIGHT = 20
    #endregion

    #region Image Transformation
    YELLOW_PIECE_IMAGE = pygame.transform.rotate(
        pygame.transform.scale(YELLOW_PIECE_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)),
        45)
    PURPLE_PIECE_IMAGE = pygame.transform.rotate(
        pygame.transform.scale(PURPLE_PIECE_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT)),
        -45)
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    #endregion

    #region Player settings
    PLAYER_1_KEYS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]    # left, right, up, down
    PLAYER_2_KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    PLAYER_1_MAX_HEALTH = 10
    PLAYER_2_MAX_HEALTH = 10
    #endregion
