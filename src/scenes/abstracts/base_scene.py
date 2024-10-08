import pygame as pg

from abc import ABC

from src.commons.constants import BASE_COLOR
from src.commons.helpers import get_color
from src.scenes.interfaces import IScene


class BaseScene(IScene, ABC):
    def __init__(self, game: 'Game', **kwargs):
        self.running = False
        self.game = game
        # todo: arreglar todooo lo del fondo en las escenas
        #       actualmente es un sprite, necesito que se instancie
        #       en cada escena, y que cada escena use el fondo
        #       que se le pase como argumento, si no se le pasa
        #       fondo, se debe usar una superficie con el color
        #       base del juego definido en constants.py

        bg = pg.Surface(self.game.get_screen().get_size()).fill(get_color(BASE_COLOR))
        self.background = kwargs.get('background', bg)

        self.music = kwargs.get('music', None)

    def change_scene(self, scene: 'Scene'):
        self.game.set_scene(scene)

    def stop_running(self):
        self.running = False

    def startup(self):self.running = True

    def update(self, *args, **kwargs):
        self.background.update(self.game.get_delta())

    def draw(self, *args, **kwargs):
        if self.background is not None:
            self.background
        # bg_color = get_color(kwargs.get('bg', BASE_COLOR))
        #
        # self.game.screen.fill(bg_color)
