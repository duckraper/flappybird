import pygame as pg

from abc import ABC

from src.entities.interfaces import ISolidSprite


class SolidSprite(pg.sprite.Sprite,
                  ISolidSprite,
                  ABC):
    """
    interface for clasifying sprites as solid ones
    when no physics needs to be applied to them
    """
    pass
