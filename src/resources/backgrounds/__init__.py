from pygame.transform import scale

from src.commons.assets_loader import AssetsLoader, ASSETS_DIR
from src.commons.constants import BG_SIZE
from src.core.game.settings import SCREEN_SIZE

BG_DIR = ASSETS_DIR.joinpath('images').joinpath('backgrounds')

backgrounds = [
    scale(AssetsLoader.load_image(bg), BG_SIZE)
    for bg in list(BG_DIR.iterdir())
]
