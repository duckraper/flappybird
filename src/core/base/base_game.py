from abc import ABC, abstractmethod

import pygame as pg

from src.core.settings import SCREEN_SIZE, GAME_TITLE


# abstract class
class BaseGame(ABC):
    def __init__(self, *args, **kwargs):
        self.running: bool = False
        self.screen: pg.surface.Surface = pg.display.set_mode(SCREEN_SIZE)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.title = kwargs.get('title', GAME_TITLE)
        self.icon: pg.surface.Surface = kwargs.get('icon', None)

    def startup(self):
        pg.display.set_caption(self.title)
        pg.display.set_icon(self.icon) if self.icon else None

        self.running = True

    def stop_running(self):
        print('game closed...')
        self.running = False

    def get_screen(self):
        return self.screen

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def run(self):
        pass
