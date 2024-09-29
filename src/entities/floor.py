from random import choice

import pygame as pg

from src.utils.spritesheets.floor import floor_spritesheet
from . import BaseSprite
from ..core.settings import FLOOR_Y, DIFFICULTY_LEVELS


class Floor(BaseSprite):
    def __init__(self, x=0, y=FLOOR_Y, speed=DIFFICULTY_LEVELS['medium']['speed']):
        self.speed = speed

        kind_choice = choice(list(floor_spritesheet.keys()))
        image = floor_spritesheet[kind_choice]
        super().__init__(image, x, y)

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pg.mask.from_surface(self.image)

    def constraints(self):
        if self.rect.right < 0:
            self.kill()

    def update(self, delta):
        self.x -= self.speed * delta
        self.rect.x = self.x

        self.constraints()
