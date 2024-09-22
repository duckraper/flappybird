from pathlib import Path

import pygame as pg

from src.core.settings import SCREEN_HEIGHT

BASE_DIR = Path(__file__).resolve().parent.parent  # src/
ASSETS_DIR = BASE_DIR.joinpath('assets')  # src/assets

DEFAULT_SPRITE_SIZE: tuple[int, int] = (SCREEN_HEIGHT // 15, SCREEN_HEIGHT // 15)


FONTS_DIR = BASE_DIR.parent.joinpath('assets', 'fonts')  # ../assets/fonts

pg.font.init()

FONT_FILENAME = 'FlappyBirdRegular-9Pq0.ttf'
DEFAULT_FONT_SIZE = 20
DEFAULT_FONT_STYLE = pg.font.Font(FONTS_DIR.joinpath(FONT_FILENAME), DEFAULT_FONT_SIZE)

COLORS = {
    "blue": (32, 41, 135),
    "sky_blue": (64, 188, 216),
    "black": (18, 22, 25),
    "less_black": (24, 25, 29),
    "jasmine": (244, 213, 141),
    "pink": (147, 47, 109),
    "gray": (154, 160, 168),
    "red": (135, 27, 27),
    "white": (255, 255, 255),
    "honeydew": (225, 239, 230)
}

DEFAULT_TITLE_FONT_SIZE = 150
DEFAULT_TITLE_FONT_COLOR = 'white'
DEFAULT_OPTION_FONT_SIZE = 80
DEFAULT_OPTION_FONT_COLOR = 'honeydew'
DEFAULT_HOVER_OPTION_FONT_SIZE = DEFAULT_OPTION_FONT_SIZE + DEFAULT_OPTION_FONT_SIZE // 10
DEFAULT_HOVER_OPTION_FONT_COLOR = 'white'
DEFAULT_OPTIONS_OFFSET = 60
DEFAULT_OUTLINE_WIDTH = 2
DEFAULT_SHADOW_WIDTH = 3
DEFAULT_OUTLINE_COLOR = (0, 0, 0)

BASE_COLOR = COLORS['honeydew']
