import pygame as pg

from abc import ABC, abstractmethod


class BaseSprite(pg.sprite.Sprite,
                 ABC):
    def __init__(self, image: pg.Surface, x: int, y: int):
        super().__init__()
        self.image: pg.Surface = image
        self.x = x
        self.y = y
        self.rect: pg.Rect = self.image.get_rect(center=(self.x, self.y))

    @abstractmethod
    def update(self, delta):
        pass

    # @abstractmethod
    # def draw(self, screen: pg.surface.Surface):
    #     pass
