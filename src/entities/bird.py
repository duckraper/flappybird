from random import choice

import pygame as pg

from src.core.physics import Physics
from src.utils.constants import COLORS
from .abstracts.animated_sprite import AnimatedSprite
from ..core.settings import SCREEN_HEIGHT
from src.utils.spritesheets.bird import bird_spritesheet, birds_colors


class Bird(AnimatedSprite):
    def __init__(self, x: int, y: int):
        spritesheet = bird_spritesheet[choice(birds_colors)]

        super().__init__(x, y, 16, *spritesheet)

        self.rect: 'Rect' = self.image.get_rect(center=(self.x, self.y))
        self.mask = pg.mask.from_surface(self.image)
        self.physics = Physics()

    def constraints(self):
        if self.rect.top < 0:
            self.y = 0 + self.image.get_height() // 2
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.image.get_height() // 2
            self.rect.bottom = SCREEN_HEIGHT

    def jump(self):
        self.current_frame = 0
        if not self.animating:
            self.animating = True

        self.physics.jump()

    def update(self, delta: float):
        super().update(delta)

        self.y = self.physics.update_position(self.y, delta)
        self.rect.center = (self.x, self.y)

        self.constraints()
