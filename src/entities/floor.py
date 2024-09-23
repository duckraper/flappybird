import pygame as pg

from . import BaseSprite
from ..core.settings import FLOOR_Y, SCREEN_WIDTH, FLOOR_HEIGHT
from ..utils.helpers import get_color


class Floor(BaseSprite):
    def __init__(self, x=0, y=FLOOR_Y):
        image = pg.Surface((SCREEN_WIDTH, FLOOR_HEIGHT))
        image.fill(get_color('jasmine'))

        super().__init__(image, x, y)

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, delta):
        pass

