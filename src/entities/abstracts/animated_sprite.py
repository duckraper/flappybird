from abc import ABC

from src.entities import BaseSprite
from src.entities.interfaces import IAnimatedSprite


class AnimatedSprite(BaseSprite,
                     IAnimatedSprite,
                     ABC):
    def __init__(self, x: int, y: int, animation_speed: int, *spritesheet):
        self.animation_speed = animation_speed
        self.current_frame = 0
        self.spritesheet = spritesheet
        self.animating = False

        image = self.spritesheet[self.current_frame]
        super().__init__(image, x, y)

    def get_current_frame(self) -> int:
        return int(self.current_frame)

    def set_current_frame(self, frame: int) -> None:
        self.current_frame = frame

    def get_animating(self) -> bool:
        return self.animating

    def set_animating(self, animating: bool) -> None:
        self.animating = animating

    def animate(self, delta):
        if self.animating:
            self.current_frame += self.animation_speed * delta % len(self.spritesheet)
            if self.current_frame >= len(self.spritesheet):
                self.set_current_frame(0)
                self.set_animating(False)
            self.image = self.spritesheet[self.get_current_frame()]

    def update(self, delta):
        self.animate(delta)
