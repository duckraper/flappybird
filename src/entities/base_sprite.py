from pygame.sprite import Sprite
from abc import ABC, abstractmethod


class BaseSprite(Sprite,
                 ABC):
    def __init__(self, image: 'Surface', x: int, y: int):
        super().__init__()
        self.image: 'Surface' = image
        self.x = x
        self.y = y

    @abstractmethod
    def update(self, delta):
        pass
