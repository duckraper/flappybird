from random import choice
from time import time

import pygame as pg

from src.core.game.settings import DIFFICULTY_LEVELS
from src.entities.abstracts.moving_sprite import MovingSprite
from src.entities.spritesheets import pipe_spritesheet


class Pipe(MovingSprite):
    def __init__(self, x, y, upside_down: bool = False, speed=DIFFICULTY_LEVELS['medium']['speed']):
        self.speed = speed

        image = pipe_spritesheet[choice(list(pipe_spritesheet.keys()))]

        super().__init__(speed, image, x, y)

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
        super().update(delta)

        self.constraints()
