from abc import ABC

import pygame as pg

from src.entities.sprites.interfaces import IMovingSprite


class MovingSprite(pg.sprite.Sprite,
                   IMovingSprite,
                   ABC):
    def __init__(self, vx=0, vy=0):
        self.vx = vx
        self.vy = vy
        self.__moving = True

    def get_speed(self) -> float:
        return self.vx

    def set_speed(self, vx: float = 0, vy: float = 0) -> None:
        self.vx = vx
        self.vy = vy

    def get_moving(self) -> bool:
        return self.__moving

    def set_moving(self, moving: bool) -> None:
        self.__moving = moving

    def move_x(self, delta):
        if self.get_moving():
            self.x += self.vx * delta
            self.rect.x = self.x

    def move_y(self, delta):
        if self.get_moving():
            self.y += self.vy * delta
            self.rect.y = self.y

    def move(self, delta):
        self.move_x(delta)
        self.move_y(delta)
