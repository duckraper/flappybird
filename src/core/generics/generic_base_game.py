import pygame as pg
from src.core.settings import SCREEN_SIZE

# abstract class
class BaseGame:
    def __init__(self, *args, **kwargs):
        self.running: bool = True
        self.screen: pg.Surface = pg.display.set_mode(SCREEN_SIZE)
        self.clock: pg.time.Clock = pg.time.Clock()

    def stop_running(self):
        self.running = False

    def get_screen(self):
        return self.screen

    def update(self):
        pass

    def run(self):
        pass
