import pygame as pg
from pygame.sprite import collide_mask


class CollisionDetectionMixin:
    def collided(self, sprite, group):
        collided_sprite = pg.sprite.spritecollide(sprite, group, False, collided=collide_mask)

        return bool(collided_sprite)

    # return whos colliding with
    def collided_with(self, sprite, group):
        collided_sprite = pg.sprite.spritecollide(sprite, group, False, collided=collide_mask)

        return collided_sprite
