from random import choice

import pygame as pg

from src.commons.constants import FLOOR_Y
from src.core.game.settings import DIFFICULTY_LEVELS
from src.entities.abstracts.moving_sprite import MovingSprite
from src.resources.spritesheets import floor_spritesheet


class Floor(MovingSprite):
    def __init__(self, x=0, y=FLOOR_Y, speed=DIFFICULTY_LEVELS['medium']['speed']):
        self.speed = speed

        kind_choice = choice(list(floor_spritesheet.keys()))
        image = floor_spritesheet[kind_choice]
        super().__init__(speed, image, x, y)

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pg.mask.from_surface(self.image)

    def constraints(self):
        if self.rect.right < 0:
            self.kill()

    def update(self, delta):
        super().update(delta)

        self.constraints()
