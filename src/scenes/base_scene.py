import pygame as pg


class BaseScene:
    def __init__(self, game):
        self.running = True
        self.game = game

    def get_input(self):
        pass

    def draw(self):
        pass

    def update(self):
        self.get_input()
