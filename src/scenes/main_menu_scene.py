import pygame as pg
from .base_menu_scene import BaseMenuScene
from src.utils.helpers import get_font
from ..utils import COLORS


class MainMenuScene(BaseMenuScene):
    def __init__(self, game):
        options_list = [
            "Start",
            "Quit"
        ]
        super().__init__(game, game.title, *options_list)

    def draw(self):
        self.game.screen.blit(self.title_font_surface, self.title_font_surface.get_rect(center=(400, 350)))

    def perform_start(self):
        print('starting...')

    def perform_quit(self):
        self.game.stop_running()
