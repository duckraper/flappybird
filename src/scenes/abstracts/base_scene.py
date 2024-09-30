from abc import ABC

from src.commons.constants import BASE_COLOR
from src.commons.helpers import get_color
from src.scenes.interfaces import IScene


class BaseScene(IScene, ABC):
    def __init__(self, game: 'Game'):
        self.running = False
        self.game = game

    def stop_running(self):
        self.running = False

    def startup(self):
        self.running = True

    def draw(self, *args, **kwargs):
        bg_color = get_color(kwargs.get('bg_color', BASE_COLOR))

        self.game.screen.fill(bg_color)
