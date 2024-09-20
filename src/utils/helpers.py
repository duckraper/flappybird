from pathlib import Path

import pygame as pg

from src.core.settings import KEY_BINDINGS
from .constants import FONTS_DIR, DEFAULT_FONT_SIZE, ASSETS_DIR, DEFAULT_SPRITE_SIZE


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


def get_font(font_name: str = 'Pixeled.ttf',
             font_size: int = DEFAULT_FONT_SIZE) -> pg.font.Font:
    return pg.font.Font(FONTS_DIR.joinpath(font_name), font_size)


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
