from abc import ABC, abstractmethod

from src.entities import BaseSprite


class AnimatedSprite(BaseSprite,
                     ABC):
    def __init__(self, x: int, y: int, animation_speed: int, *spritesheet):
        self.animation_speed = animation_speed
        self.current_frame = 0
        self.spritesheet = spritesheet
        self.animating = False

        image = self.spritesheet[self.current_frame]
        super().__init__(image, x, y)

    def animate(self, delta):
        if self.animating:
            self.current_frame += self.animation_speed * delta % len(self.spritesheet)
            if self.current_frame >= len(self.spritesheet):
                self.current_frame = 0
                self.animating = False
            self.image = self.spritesheet[int(self.current_frame)]

    def update(self, delta):
        self.animate(delta)
