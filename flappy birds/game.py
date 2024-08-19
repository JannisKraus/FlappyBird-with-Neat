import pygame
from bird import Bird
from tube import Tube

from settings import *

pygame.init()

class Game:

    def __init__(self, window):
        self.window = window
        self.bird = Bird(window, WIN_HEIGHT / 2)
        self.jumping = False

        self.tube_manager = Tube(self.window)

        self.score = 0
        self.hidden_score = 0
    
    # game logic

    def draw(self):
        if BG_IMG is None:
            self.window.fill(WHITE)
        else:
            self.window.blit(BG_IMG, (0, 0))
        
        self.bird.draw()
        self.draw_score()
        self.tube_manager.draw()

        pygame.display.update()
        self.bird_rect = pygame.Rect(self.bird.x, self.bird.y, 64, 64)
    
    def draw_text(self, text, x, y, color = BLACK):
        text = FONT.render(text, False, color)
        x = x - text.get_width() // 2
        self.window.blit(text, (x, y))
    
    def draw_score(self):
        self.draw_text(str(self.score), WIN_WIDTH // 2, 30)
    
    def move_bird(self, keys):
        bird_jump = pygame.K_SPACE

        self.bird.gravity += 1
        self.bird.y += self.bird.gravity

        if keys[bird_jump]:
            self.bird.gravity = -bird_jump_size
    
    def handle_collision(self):
        if self.bird_rect.bottom >= WIN_HEIGHT or self.bird_rect.top <= 0:
            return True
        
        return self.tube_manager.check_tube_collision(self.bird_rect)
    
    def draw_winning_text(self):
        self.draw()
        self.draw_text("You Won!", WIN_WIDTH // 2, WIN_HEIGHT // 2 - 90)
        pygame.display.update()
        pygame.time.delay(1000)
    
    def draw_losing_text(self):
        self.draw()
        self.draw_text("You LOSE!", WIN_WIDTH // 2, WIN_HEIGHT // 2 - 90)
        pygame.display.update()
        pygame.time.delay(1000)
    
    def check_winning_condition(self):
        if self.score >= WINNING_SCORE:
            self.draw_winning_text()
            return True
            
    
    # neural network

    def move_bird_network(self, network_output):
        if network_output == 0:
            pass
        elif network_output == 1:
            self.bird.gravity = -bird_jump_size