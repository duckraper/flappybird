from abc import ABC, abstractmethod

import pygame as pg

from src.core.game.settings import SCREEN_SIZE, GAME_TITLE


class BaseGame(ABC):
    def __init__(self, *args, **kwargs):
        self.running: bool = False
        self.screen: 'Surface' = pg.display.set_mode(size=SCREEN_SIZE,
                                                              flags=kwargs.get('flags', 0))
        self.clock: 'Clock' = pg.time.Clock()
        self.title: str = kwargs.get('title', GAME_TITLE)
        self.icon: 'Surface' = kwargs.get('icon', None)

    def startup(self):
        pg.display.set_caption(self.title)
        pg.display.set_icon(self.icon) if self.icon else None

        self.running = True

    def stop_running(self):
        self.running = False

    def get_screen(self):
        return self.screen

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def run(self):
        pass
