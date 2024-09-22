from pathlib import Path
from functools import lru_cache

import pygame as pg

from src.core.settings import KEY_BINDINGS
from . import FONT_FILENAME
from .constants import FONTS_DIR, DEFAULT_FONT_SIZE, ASSETS_DIR, DEFAULT_SPRITE_SIZE, COLORS


@lru_cache(maxsize=128)
def render_text_with_outline(text, font, text_color, **kwargs):
    outline_color = get_color(kwargs.get('outline_color', (0, 0, 0)))
    outline_width = kwargs.get('outline_width', 2)
    shadow_width = kwargs.get('shadow_width', 3)

    text_surface = font.render(text, True, text_color)

    outline_surface = pg.Surface((text_surface.get_width() + 2 * outline_width,
                                  text_surface.get_height() + 2 * outline_width),
                                 pg.SRCALPHA)

    # render outline by blitting multiple times
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width * shadow_width + 1):
            if dx != 0 or dy != 0:  # skip center
                outline_surface.blit(font.render(text, True, outline_color),
                                     (dx + outline_width, dy + outline_width))

    outline_surface.blit(text_surface, (outline_width, outline_width))

    return outline_surface

def is_pressed(events, key: str | list[str] = 'any') -> bool:
    try:
        for event in events:
            if event.type == pg.KEYDOWN:
                if key == 'any':
                    return True
                if isinstance(key, list):
                    return any(event.key == KEY_BINDINGS.get(k) for k in key)
                return event.key == KEY_BINDINGS.get(key)
    except KeyError as e:
        raise ValueError(f"Key '{key}' not found in KEY_BINDINGS")

    return False


def get_font(font_name: str = FONT_FILENAME,
             font_size: int = DEFAULT_FONT_SIZE) -> pg.font.Font:
    return pg.font.Font(FONTS_DIR.joinpath(font_name), font_size)

def get_color(color: str | tuple) -> tuple:
    if isinstance(color, str):
        try:
            return COLORS[color]
        except KeyError:
            raise ValueError(f"Color {color} not found in COLORS")
    return color

def is_between(value: float | int, minimum: int, maximum: int):
    return minimum <= value <= maximum


def load_image(filepath: Path | str) -> pg.surface.Surface:
    return pg.image.load(filepath).convert_alpha()


def load_sprites(directory: Path | str,
                 file_pattern: str,
                 size: tuple[int, int] = DEFAULT_SPRITE_SIZE,
                 colorkey=None) -> list[pg.surface.Surface]:
    """
     Usage:
        sprite = load_sprites("path/to/spritesheet", "sprite_name-0{n}.png", (50, 50), (0, 0, 0))
        where n is the number of the sprite frame
    """
    imgs_dir: Path = ASSETS_DIR.joinpath('images', directory)

    sprite_list: list[pg.surface.Surface] = []
    files_amount: int = len(list(imgs_dir.iterdir()))

    for i in range(files_amount):
        sprite_path: Path = imgs_dir.joinpath(file_pattern.format(n=i))
        frame: pg.surface.Surface = pg.transform.scale(load_image(str(sprite_path)), size)

        if colorkey is not None:
            frame.set_colorkey(colorkey)

        sprite_list.append(frame)

    return sprite_list
