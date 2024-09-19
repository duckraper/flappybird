from pathlib import Path

import pygame as pg

from src.core.settings import SCREEN_HEIGHT

BASE_DIR = Path(__file__).resolve().parent.parent  # src/
ASSETS_DIR = BASE_DIR.joinpath('assets')  # src/assets

DEFAULT_SPRITE_SIZE: tuple[int, int] = (SCREEN_HEIGHT // 15, SCREEN_HEIGHT // 15)

DEFAULT_FONT_SIZE = 20
FONTS_DIR = BASE_DIR.parent.joinpath('assets', 'fonts')  # ../assets/fonts

pg.font.init()

DEFAULT_FONT = pg.font.Font(FONTS_DIR.joinpath('Pixeled.ttf'), DEFAULT_FONT_SIZE)

COLORS = {
    "blue": (32, 41, 135),
    "sky_blue": (32, 41, 100),
    "black": (18, 22, 25),
    "less_black": (24, 25, 29),
    "jasmine": (244, 213, 141),
    "pink": (147, 47, 109),
    "gray": (154, 160, 168),
    "red": (135, 27, 27),
    "white": (230, 230, 230)
}

BASE_COLOR = COLORS['white']
