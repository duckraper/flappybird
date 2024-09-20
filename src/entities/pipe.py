import pygame as pg

from ..utils.constants import COLORS
from .base_sprite import BaseSprite


class Pipe(BaseSprite):
    def __init__(self, x , y, upside_down: bool):
        image = pg.Surface((50, 50))
        image.fill(COLORS['red'])

        super().__init__(image, x, y)

    def update(self, delta):
        pass
