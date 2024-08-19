import datetime
import os

import pygame

pygame.init()

# Game Settings
WIN_WIDTH, WIN_HEIGHT = 1500, 844
FPS = 60
FONT = pygame.font.SysFont("comicsans", 50)

# Color converter: https://www.rapidtables.com/convert/color/rgb-to-hex.html
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Decide if you want to use a background image.
BG_IMG = None
WINNING_SCORE = 10

BIRD_IMG_Path = "imgs/bird.png"
bird_jump_size = 15

tube_width = 100
tube_gap = 250
tube_speed = 7
tube_time = 2.5