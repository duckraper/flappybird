import pygame as pg

from src.core.generics import BaseGame
from src.core.mixins import EventManagerMixin, SpriteManagerMixin, SceneManagerMixin
from src.core.mixins.delta_time_manager_mixin import DeltaTimeManagerMixin
from src.core.settings import FPS, DIFFICULTY_LEVELS
from src.scenes import MainMenuScene
from src.utils import Debug, BASE_COLOR


class Game(EventManagerMixin,
           DeltaTimeManagerMixin,
           SceneManagerMixin,
           BaseGame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debugger = Debug()
        self.scene = None

        self.difficulty = 'medium'
        self.high_score = 0

        self.startup()

    def startup(self):
        super().startup()

        self.set_scene(MainMenuScene(game=self))

    def perform_rendering(self):
        self.screen.fill(BASE_COLOR)
        self.draw_scene()
        self.debugger.draw(info=f'delta: {round(self.get_delta(), 3)}')

        pg.display.flip()

    def update(self):
        self.process_events_but_input()
        self.update_scene()

        self.update_delta()

    def run(self):
        while self.running:
            self.update()
            self.perform_rendering()
            self.clock.tick(FPS)

        pg.quit()

