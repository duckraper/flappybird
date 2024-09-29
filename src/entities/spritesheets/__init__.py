import pygame as pg

from src.core.game.settings import BIRD_SIZE, FLOOR_SIZE, PIPES_SIZE
from src.utils.assets_loader import AssetsLoader

birds_colors = ['blue', 'brown', 'green', 'orange', 'purple', 'red', 'white']
pipes_colors = ['orange', 'green']

bird_spritesheet = {
    color: AssetsLoader.load_sprites(directory=f'bird/{color}',
                                     file_pattern=f'{color}-bird-0{{i}}.png',
                                     size=BIRD_SIZE)
    for color in birds_colors
}

floor_spritesheet = {
    'normal': AssetsLoader.load_sprites(directory="floor",
                                        file_pattern="floor-0{i}.png",
                                        size=FLOOR_SIZE),
    'inverted': pg.transform.flip(
        AssetsLoader.load_sprites(directory="floor",
                                  file_pattern="floor-0{i}.png",
                                   size=FLOOR_SIZE), True, False)
}

pipe_spritesheet = {
    color: AssetsLoader.load_sprites(directory=f'pipes/{color}',
                                     file_pattern=f'{color}-pipe-0{{i}}.png',
                                     size=PIPES_SIZE)
    for color in pipes_colors
}
