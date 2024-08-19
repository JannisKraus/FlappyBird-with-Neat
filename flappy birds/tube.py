import pygame
import random

from settings import *

class Tube:
    def __init__(self, window):
        self.window = window

        self.tube_width = tube_width
        self.tube_gap = tube_gap
        self.tube_speed = tube_speed

        self.temp = random.randint(50, WIN_HEIGHT - self.tube_gap - 50) #one use tube height

        self.tubes = [{'x':WIN_WIDTH,
                       'top_height': self.temp,
                       'bottom_height': WIN_HEIGHT - self.temp - self.tube_gap
                       }]
        self.ticks = 0
    
    def update(self):
        for tube in self.tubes:
            tube['x'] -= self.tube_speed
            if tube['x'] < -self.tube_width: #TODO maybe change?
                self.tubes.remove(tube)
        
        self.ticks += 1

        if (self.ticks / 60) >= tube_time:
            self.add_tube()
            self.ticks = 0
    
    def add_tube(self):
        tube_height = random.randint(50, WIN_HEIGHT - self.tube_gap - 50)
        self.tubes.append({
            'x': WIN_WIDTH,
            'top_height': tube_height,
            'bottom_height': WIN_HEIGHT - tube_height - self.tube_gap
            })
    
    def check_tube_collision(self, bird_rect):
        for tube in self.tubes:
            top_tube_rect = pygame.Rect(tube['x'], 0, self.tube_width, tube['top_height'])
            bottom_tube_rect = pygame.Rect(tube['x'], tube['top_height'] + self.tube_gap, self.tube_width, tube['bottom_height'])
            
            if bird_rect.colliderect(top_tube_rect) or bird_rect.colliderect(bottom_tube_rect):
                return True
            return False
    
    def draw(self):
        for tube in self.tubes:
            pygame.draw.rect(self.window, GREEN, (tube['x'], 0, self.tube_width, tube['top_height']))
            pygame.draw.rect(self.window, GREEN, (tube['x'], tube['top_height'] + self.tube_gap, self.tube_width, tube['bottom_height']))