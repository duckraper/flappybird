import pygame as pg

from time import time

from src.core.game.settings import SCREEN_SIZE
from src.entities.sprites.abstracts import SolidSprite, CommonSprite


class Blink(SolidSprite,
            CommonSprite):
    def __init__(self, color, duration=0.5, alpha=200):
        self.color = color
        self.duration = duration
        self.alpha = alpha
        self.start_time = time()
        self.surface = pg.Surface(SCREEN_SIZE)
        self.surface.fill(color)
        self.surface.set_alpha(alpha)

        CommonSprite.__init__(self, self.surface, 0, 0, hasnt_mask=True)

    def constraints(self) -> None:
        if time() - self.start_time > self.duration:
            self.kill()

    def update(self, *args, **kwargs):
        self.constraints()
