from abc import ABC

from pygame.sprite import Sprite

from src.entities.interfaces import ISprite


class BaseSprite(Sprite,
                 ISprite,
                 ABC):
    def __init__(self, image: 'Surface', x: int, y: int):
        super().__init__()
        self.image: 'Surface' = image
        self.x = x
        self.y = y

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
