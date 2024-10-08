from pygame.sprite import Group

from src.commons.constants import GRAVITY_FORCE
from src.entities.sprites.abstracts import SolidSprite


class Physics:
    def __init__(self, gravity: float = GRAVITY_FORCE):
        self.gravity = gravity

    def apply_gravity(self, sprite_group: 'Group', delta: float):
        for sprite in sprite_group.sprites():
            if isinstance(sprite, SolidSprite):
                continue
            if hasattr(sprite, 'vy'):
                sprite.vy += self.gravity * delta
                sprite.y += sprite.vy * delta
                sprite.rect.center = (sprite.x, sprite.y)
