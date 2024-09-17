import pygame as pg
from pathlib import Path
from .constants import FONTS_DIR, DEFAULT_FONT_SIZE, ASSETS_DIR, DEFAULT_SPRITE_SIZE
from src.core.settings import KEY_BINDINGS

def is_pressed(key: str='any') -> bool:
    if key == 'any':
        return any(pg.key.get_pressed())
    return pg.key.get_pressed()[KEY_BINDINGS[key]]

def get_font(font_name: str='Pixeled.ttf',
             font_size: int=DEFAULT_FONT_SIZE) -> pg.font.Font:
    return pg.font.Font(FONTS_DIR.joinpath(font_name), font_size)

def is_between(value: float | int, minimum: int, maximum: int):
    return minimum <= value <= maximum

def load_image(filepath: Path | str) -> pg.surface.Surface:
    return pg.image.load(filepath).convert_alpha()

def load_sprites(directory: Path | str,
                 file_pattern: str,
                 size: tuple[int, int]=DEFAULT_SPRITE_SIZE,
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
