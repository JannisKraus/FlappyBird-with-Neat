import pygame
from settings import *

class Bird:

    def __init__(self, window, y):
        self.window = window
        self.sprite = pygame.image.load(BIRD_IMG_Path)

        self.y = y
        self.x = 150

        self.gravity = 0
    
    def draw(self):
        self.window.blit(self.sprite, (self.x, self.y))