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
        self.background = kwargs.get('background', None)

    def stop_running(self):
        self.running = False

    def startup(self):
        self.running = True

    def draw(self, *args, **kwargs):
        bg_color = get_color(kwargs.get('bg', BASE_COLOR))

        self.game.screen.fill(bg_color)
