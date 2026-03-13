import os

import pygame


pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class Options:
    #region Game settings
    FPS = 60
    WIDTH, HEIGHT = 900, 500
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

    #region Fonts
    HEALTH_FONT = 'comicsans'
    #endregion

    #region Sounds
    SWING_SOUND = pygame.mixer.Sound(os.path.join('assets', 'gun_sound.mp3'))
    SWING_SOUND.set_volume(0.2)   # lower volume
    TARGET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit_sound.mp3'))
    #endregion

    #region Images
    YELLOW_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'yellow.png'))
    PURPLE_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'purple.png'))
    BACKGROUND = pygame.image.load(os.path.join('assets', 'space.png'))
    #endregion

    #region Player settings
    PIECE_WIDTH = 20
    PIECE_HEIGHT = 20
    PLAYER_1_KEYS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]    # left, right, up, down
    PLAYER_2_KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    #endregion
