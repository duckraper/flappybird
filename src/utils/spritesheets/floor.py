import pygame as pg

from src.core.settings import FLOOR_SIZE
from src.utils.assets_loader import AssetsLoader

floor_spritesheet = {
    'normal': AssetsLoader.load_sprites("floor", "floor-0{i}.png", FLOOR_SIZE),
    'inverted': pg.transform.flip(AssetsLoader.load_sprites(
        "floor", "floor-0{i}.png", FLOOR_SIZE), True, False)
}
