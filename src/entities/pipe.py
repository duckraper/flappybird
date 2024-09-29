import pygame as pg

from time import time

from src.entities.abstracts.base_sprite import BaseSprite
from ..core.settings import DIFFICULTY_LEVELS
from ..utils.spritesheets.pipe import pipe_spritesheet


class Pipe(BaseSprite):
    def __init__(self, x, y, color: str, upside_down: bool = False, speed=DIFFICULTY_LEVELS['medium']['speed']):
        self.speed = speed

        if color not in ['orange', 'green']:
            raise ValueError('Invalid color for pipe, only orange and green are allowed')

        image = pipe_spritesheet[color]

        super().__init__(image, x, y)

        if upside_down:
            self.rect: 'Rect' = self.image.get_rect(midbottom=(self.x, self.y))
        else:
            self.rect: 'Rect' = self.image.get_rect(midtop=(self.x, self.y))

        self.mask = pg.mask.from_surface(self.image)
        self.spawn_time = time()

    def constraints(self):
        if self.rect.right < -self.rect.width:
            self.kill()

    def update(self, delta):
        self.x -= self.speed * delta
        self.rect.x = self.x

        self.constraints()
