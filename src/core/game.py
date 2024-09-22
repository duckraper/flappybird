import pygame as pg

from src.core.base import BaseGame
from src.core.mixins import EventManagerMixin, SceneManagerMixin
from src.core.mixins.delta_time_manager_mixin import DeltaTimeManagerMixin
from src.core.settings import FPS
from src.scenes.menus.main_menu_scene import MainMenuScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene
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

    @property
    def is_paused(self) -> bool:
        return isinstance(self.scene, PauseMenuScene)

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

