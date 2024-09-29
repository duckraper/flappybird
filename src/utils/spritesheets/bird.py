from src.core.settings import BIRD_SIZE
from src.utils.assets_loader import AssetsLoader

birds_colors = ['blue', 'brown', 'green', 'orange', 'purple', 'red', 'white']

bird_spritesheet = {
    color: AssetsLoader.load_sprites(directory=f'bird/{color}',
                                     file_pattern=f'{color}-bird-0{{i}}.png',
                                     size=BIRD_SIZE)
    for color in birds_colors
}
