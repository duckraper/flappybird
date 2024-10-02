from pygame.transform import scale
from src.commons.assets_loader import AssetsLoader, ASSETS_DIR
from src.core.game.settings import SCREEN_SIZE

BG_DIR = ASSETS_DIR.joinpath('images').joinpath('backgrounds')

backgrounds = [
    scale(AssetsLoader.load_image(bg), SCREEN_SIZE)
    for bg in list(BG_DIR.iterdir())
]
