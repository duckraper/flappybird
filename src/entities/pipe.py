import pygame as pg

from .base_sprite import BaseSprite
from ..core.settings import DIFFICULTY_LEVELS, SCREEN_HEIGHT
from ..utils.helpers import get_color


class Pipe(BaseSprite):
    def __init__(self, x, y, upside_down: bool = False, speed=DIFFICULTY_LEVELS['medium']['speed']):
        self.speed = speed

        image = pg.Surface((80, SCREEN_HEIGHT))
        image.fill(get_color('green'))

        super().__init__(image, x, y)

        if upside_down:
            self.rect: 'Rect' = self.image.get_rect(midbottom=(self.x, self.y))
        else:
            self.rect: 'Rect' = self.image.get_rect(midtop=(self.x, self.y))

    def update(self, delta):
        self.x -= self.speed * delta
        self.rect.x = self.x

        if self.x < -self.rect.width:
            self.kill()
