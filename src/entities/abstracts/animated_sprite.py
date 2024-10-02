from abc import ABC

import pygame as pg

from src.entities.interfaces import IAnimatedSprite


class AnimatedSprite(pg.sprite.Sprite,
                     IAnimatedSprite,
                     ABC):
    def __init__(self, fps: int, *spritesheet):
        self._fps = fps
        self.__current_frame = 0
        self.__spritesheet = spritesheet
        self.__animating = False

        self.image = self.__spritesheet[self.__current_frame]
        self.mask = pg.mask.from_surface(self.image)

    def get_current_frame(self) -> int:
        return int(self.__current_frame)

    def set_current_frame(self, frame: int) -> None:
        self.__current_frame = frame

    def get_animating(self) -> bool:
        return self.__animating

    def set_animating(self, animating: bool) -> None:
        self.__animating = animating

    def animate(self, delta):
        if self.__animating:
            self.__current_frame += self._fps * delta % len(self.__spritesheet)
            if self.__current_frame >= len(self.__spritesheet):
                self.set_current_frame(0)
                self.set_animating(False)
            self.image = self.__spritesheet[self.get_current_frame()]
            self.mask = pg.mask.from_surface(self.image)
