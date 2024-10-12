from abc import ABC

import pygame as pg
from pygame.sprite import Group

from src.commons.constants import BASE_COLOR
from src.commons.helpers import get_color
from src.entities.sprites.background import Background
from src.scenes.interfaces import IScene


class BaseScene(IScene, ABC):
    def __init__(self, game: 'Game', **kwargs):
        self.running = False
        self.game = game

        bg_surface = pg.Surface(self.game.get_screen().get_size())
        bg_surface.fill(get_color(BASE_COLOR))
        bg = Background(bg_surface, vx=0)

        self.background = Group(kwargs.get('background', bg))
        self.music = kwargs.get('music', None)

    def change_scene(self, scene: 'Scene'):
        self.game.set_scene(scene)

    def stop_running(self):
        self.running = False

    def startup(self):
        self.running = True

    def update(self, *args, **kwargs):
        self.background.update(self.game.get_delta())

    def draw(self, *args, **kwargs):
        if self.running:
            self.background.draw(self.game.get_screen())
