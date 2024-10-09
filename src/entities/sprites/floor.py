from random import choice

from src.commons.constants import FLOOR_Y
from src.core.game.settings import DIFFICULTY_LEVELS
from src.entities.sprites.abstracts import MovingSprite
from src.entities.sprites.abstracts import SolidSprite, CollidableSprite, CommonSprite
from src.resources.spritesheets import floor_spritesheet


class Floor(SolidSprite,
            MovingSprite,
            CollidableSprite,
            CommonSprite):
    def __init__(self, x=0, y=FLOOR_Y, speed=DIFFICULTY_LEVELS['medium']['speed']):
        image = floor_spritesheet[choice(list(floor_spritesheet.keys()))]

        MovingSprite.__init__(self, vx=-speed)
        CommonSprite.__init__(self, image, x, y, topleft=(x, y))

    def constraints(self):
        if self.rect.right < 0:
            self.kill()

    def update(self, delta):
        self.move_x(delta)

        self.constraints()
