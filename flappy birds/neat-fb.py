from operator import abs
from statistics import mean
import numpy as np
from fb import Game
import neat
import pickle

from util import load_network_from_file, plot
from settings import *

mean_fitness_values = []
max_fitness_values = []

def evaluate_genomes(genomes, config):
    for ignored, genome in genomes:
        genome.fitness = 0

    for id, genome1 in genomes:
        game = Game(window)
        game.draw()
        train_ai(game, genome1, config)
    
    mean_fitness_values.append(mean([x[1].fitness for x in genomes]))
    max_fitness_values.append(max([x[1].fitness for x in genomes]))
    plot(mean_fitness_values, max_fitness_values)

def train_ai(game, genome1, config):
    run = True
    clock = pygame.time.Clock()
    trainee = neat.nn.FeedForwardNetwork.create(genome1, config)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        network_move(game, trainee)
        game.tube_manager.update()

        game.bird.gravity += 1
        game.bird.y += game.bird.gravity

        for tube in game.tube_manager.tubes:
            if game.bird_rect.x + game.bird_rect.width > tube['x'] and game.bird_rect.x < tube['x'] + game.tube_manager.tube_width:
                if game.bird_rect.y + game.bird_rect.height > tube['top_height'] and game.bird_rect.y < tube['top_height'] + game.tube_manager.tube_gap:
                    game.hidden_score += 1
        if game.hidden_score == 24:
            game.score += 1
            game.hidden_score = 0

        game.draw()

        if game.handle_collision():
            calculate_fitness(genome1, game.score)
            break

def network_move(game, network):
    inputs = get_network_inputs(game)
    output = network.activate(inputs)

    max_value = 0
    max_index = 0
    current_index = 0
    for output_value in output:
        if output_value > max_value:
            max_value = output_value
            max_index = current_index
        current_index += 1
    game.move_bird_network(max_index)

def get_network_inputs(game):
    return [(game.bird_rect.y + 32) / WIN_HEIGHT, (game.tube_manager.tubes[0]['top_height'] + tube_gap // 2) / WIN_HEIGHT]

def calculate_fitness(genome, rewards):
    genome.fitness = rewards


if __name__ == '__main__':
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "parameter.txt")
    configuration = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    pygame.display.set_caption("Training Mode")
    max_generations = 50

    population = neat.Population(configuration)
    #population = neat.Checkpointer.restore_checkpoint('Checkpoints/checkpoint-')

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    population.add_reporter(neat.Checkpointer(1, filename_prefix="Checkpoints/checkpoint-"))

    winner = population.run(evaluate_genomes, max_generations)
    with open('Networks/Winner.pickle', 'wb') as f:
        pickle.dumb(winner, f)
    