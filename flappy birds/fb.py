from game import Game
from settings import *

if __name__ == '__main__':
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Player Mode")
    game = Game(window)

    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        game.tube_manager.update()
        game.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()

        game.move_bird(keys)
        game.tube_manager.update()

        for tube in game.tube_manager.tubes:
            if game.bird_rect.x + game.bird_rect.width > tube['x'] and game.bird_rect.x < tube['x'] + game.tube_manager.tube_width:
                if game.bird_rect.y + game.bird_rect.height > tube['top_height'] and game.bird_rect.y < tube['top_height'] + game.tube_manager.tube_gap:
                    game.hidden_score += 1
        if game.hidden_score == 12:
            game.score += 1
            game.hidden_score = 0
    
        if game.handle_collision():
            game.draw_losing_text()
            run = False

        if game.check_winning_condition():
            run = False
    
    pygame.quit()