import pygame as pg

from src.core.physics import Physics
from src.utils.constants import COLORS
from .base_sprite import BaseSprite


class Bird(BaseSprite):
    def __init__(self, x: int, y: int):
        # Todo: implementar spritesheet, animaciones y eso
        image = pg.Surface((30, 30))
        image.fill(COLORS['red'])

        super().__init__(image, x, y)

        self.rect: 'Rect' = self.image.get_rect(center=(self.x, self.y))
        self.physics = Physics()

    def jump(self):
        self.physics.jump()

    def update(self, delta: float):
        self.y = self.physics.update_position(self.y, delta)
        self.rect.center = (self.x, self.y)
