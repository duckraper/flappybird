from abc import ABC

from .base_sprite import BaseSprite
from ..interfaces import IMovingSprite


class MovingSprite(BaseSprite, IMovingSprite, ABC):
    def __init__(self, speed, image: 'Surface', x: int, y: int):
        super().__init__(image, x, y)
        self.speed = speed
        self.moving = True

    def get_speed(self) -> float:
        return self.speed

    def set_speed(self, speed: float) -> None:
        self.speed = speed

    def get_moving(self) -> bool:
        return self.moving

    def set_moving(self, moving: bool) -> None:
        self.moving = moving

    def update(self, delta):
        if self.get_moving():
            self.x -= self.speed * delta
            self.rect.x = self.x

