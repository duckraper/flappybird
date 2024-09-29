from abc import ABC

from src.scenes.interfaces import SceneInterface
from src.utils.constants import BASE_COLOR
from src.utils.helpers import get_color


class BaseScene(SceneInterface, ABC):
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
