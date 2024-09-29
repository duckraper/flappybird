from src.utils.assets_loader import AssetsLoader
from src.core.settings import PIPES_SIZE

ORANGE = 'orange'
GREEN = 'green'

pipe_spritesheet = {
    ORANGE: AssetsLoader.load_sprites('pipes/orange', 'orange-pipe-0{i}.png', PIPES_SIZE),
    GREEN: AssetsLoader.load_sprites('pipes/green', 'green-pipe-0{i}.png', PIPES_SIZE)
}
