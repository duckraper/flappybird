from abc import ABC, abstractmethod

from pygame.sprite import Sprite


class BaseSprite(Sprite,
                 ABC):
    def __init__(self, image: 'Surface', x: int, y: int):
        super().__init__()
        self.image: 'Surface' = image
        self.x = x
        self.y = y

    @abstractmethod
    def constraints(self):
        pass

    @abstractmethod
    def update(self, delta):
        pass
