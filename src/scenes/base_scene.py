import pygame as pg
from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self, game):
        self.running = True
        self.game = game

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def update(self):
        self.get_input()
