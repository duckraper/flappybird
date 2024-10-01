import pygame as pg

from src.commons import Debug
from src.commons.constants import BASE_COLOR
from src.core.abstracts import BaseGame
from src.core.game.settings import FPS, DIFFICULTY_LEVELS
from src.core.mixins import EventManagerMixin, SceneManagerMixin
from src.core.mixins.delta_time_manager_mixin import DeltaTimeManagerMixin
from src.scenes.menus.main_menu_scene import MainMenuScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene


class Game(EventManagerMixin,
           DeltaTimeManagerMixin,
           SceneManagerMixin,
           BaseGame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debugger = Debug()
        self.scene = None

        self.difficulty = 'medium'

        self.startup()

    def startup(self):
        super().startup()

        self.set_scene(MainMenuScene(game=self))

    def set_difficulty(self, difficulty: str):
        if difficulty not in list(DIFFICULTY_LEVELS.keys()):
            raise ValueError(f'Difficulty level {difficulty} not allowed')

        self.difficulty = difficulty

    @property
    def is_paused(self) -> bool:
        return isinstance(self.scene, PauseMenuScene)

    def perform_rendering(self):
        self.screen.fill(BASE_COLOR)
        self.draw_scene()
        if self.scene.__class__.__name__ == 'GameScene':
            self.debugger.draw(info=f'score: {self.scene.manager.score}')

        pg.display.flip()

    def update(self):
        self.process_events_but_input()
        self.update_scene(delta=self.get_delta())

        self.update_delta()

    def run(self):
        while self.running:
            self.update()
            self.perform_rendering()
            self.clock.tick(FPS)

        pg.quit()
