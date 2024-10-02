import pygame as pg

from src.core.game.settings import KEY_BINDINGS, DIFFICULTY_LEVELS, DIFFICULTY
from .constants import FONT_FILENAME, FONTS_DIR, DEFAULT_FONT_SIZE, COLORS


def get_difficulty_prop(prop, difficulty=DIFFICULTY):
    return DIFFICULTY_LEVELS[difficulty][prop]

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
    if font_name == 'default':
        font_name = FONT_FILENAME

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
