from abc import ABC

import pygame as pg

from src.entities.abstracts import BaseSprite


class CommonSprite(BaseSprite,
                   ABC):
    """
    common sprite setup like setting the image, its rect, and its mask
    example usage:
       sprite = CommonSprite(image, x, y, center=(x, y))
    """

    def __init__(self, image: 'Surface', x: int, y: int, hasnt_mask: bool = False, **kwargs):
        super().__init__(x, y)
        self.image = image
        self.rect = self.image.get_rect(**kwargs)
        self.mask = pg.mask.from_surface(self.image) \
            if not hasnt_mask else None
