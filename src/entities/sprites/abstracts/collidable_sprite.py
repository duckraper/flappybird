from abc import ABC

import pygame as pg

from src.entities.sprites.interfaces import ICollidableSprite


class CollidableSprite(pg.sprite.Sprite,
                       ICollidableSprite,
                       ABC):
    def check_collision(self, other: 'Sprite', collide_mask: bool = True) -> bool:
        return bool(
            pg.sprite.collide_rect(self, other) \
                if not collide_mask \
                else pg.sprite.collide_mask(self, other)
        )

    def on_collision(self, other: 'Sprite') -> None:
        pass

    def resolve_collision(self, other: 'Sprite') -> None:
        pass
