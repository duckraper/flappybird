from random import choice

import pygame as pg

from src.core.game.settings import SCREEN_HEIGHT
from src.core.physics import Physics
from src.entities.abstracts.animated_sprite import AnimatedSprite
from src.entities.spritesheets import bird_spritesheet


class Bird(AnimatedSprite):
    def __init__(self, x: int, y: int):
        spritesheet = bird_spritesheet[choice(list(bird_spritesheet.keys()))]

        super().__init__(x, y, 16, *spritesheet)

        self.rect: 'Rect' = self.image.get_rect(center=(self.x, self.y))
        self.mask = pg.mask.from_surface(self.image)
        self.physics = Physics()

    def jump(self):
        self.set_current_frame(0)

        if not self.get_animating():
            self.set_animating(True)

        self.physics.jump()

    def constraints(self):
        if self.rect.top < 0:
            self.y = 0 + self.image.get_height() // 2
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.image.get_height() // 2
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, delta: float):
        super().update(delta)

        self.y = self.physics.update_position(self.y, delta)
        self.rect.center = (self.x, self.y)

        self.constraints()
