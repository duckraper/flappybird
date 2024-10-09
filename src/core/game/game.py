from random import choice

import pygame as pg

from src.commons import Debug
from src.commons.constants import BASE_COLOR
from src.commons.helpers import darken_image
from src.core.events import GameEvent
from src.core.game.settings import FPS, DIFFICULTY_LEVELS, SCREEN_SIZE, GAME_TITLE
from src.core.mixins import EventManagerMixin, SceneManagerMixin, SettingsManagerMixin
from src.core.mixins.delta_time_manager_mixin import DeltaTimeManagerMixin
from src.entities.sprites.background import Background
from src.resources.backgrounds import backgrounds
from src.scenes.menus.main_menu_scene import MainMenuScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene


class Game(EventManagerMixin,
           DeltaTimeManagerMixin,
           SceneManagerMixin,
           SettingsManagerMixin):
    def __init__(self, *args, **kwargs):
        self.screen_size = SCREEN_SIZE
        self.width, self.height = self.screen_size

        self.running: bool = False
        self.screen: 'Surface' = pg.display.set_mode(size=SCREEN_SIZE,
                                                     flags=kwargs.get('flags', 0))
        self.clock: 'Clock' = pg.time.Clock()
        self.title: str = kwargs.get('title', GAME_TITLE)
        self.icon: 'Surface' = kwargs.get('icon', None)

        self.debugger = Debug()
        self.content = None
        self.scene = None

        self.menus_bg_img = darken_image(choice(backgrounds).copy())
        # todo: sistema de puntaje

        self.difficulty = 'medium'

        if self.exists_config():
            self.import_config()

        self.startup()

    @staticmethod
    def post_config_change_event(config: 'str', value):
        event = GameEvent.create_config_change_event(config, value)
        pg.event.post(event)

    def startup(self):
        pg.display.set_caption(self.title)
        pg.display.set_icon(self.icon) if self.icon else None

        self.running = True

        self.set_scene(MainMenuScene(game=self, background=Background(self.menus_bg_img.copy(), vx=-100)))

    def stop_running(self):
        self.running = False

    def get_screen(self):
        return self.screen

    def set_display_mode(self, size, flags: int):
        pg.display.set_mode(size, flags)
        self.screen_size = size

    def toggle_sound(self):
        self.has_sound = not self.has_sound
        global HAS_SFX
        HAS_SFX = False

        self.post_config_change_event('has_sound', self.has_sound)

    def toggle_music(self):
        self.has_music = not self.has_music
        self.post_config_change_event('has_music', self.has_music)


    def set_difficulty(self, difficulty: str):
        if difficulty not in list(DIFFICULTY_LEVELS.keys()):
            raise ValueError(f'Difficulty level {difficulty} not allowed')

        self.difficulty = difficulty
        self.post_config_change_event('difficulty', difficulty)

    @property
    def is_paused(self) -> bool:
        return isinstance(self.scene, PauseMenuScene)

    def perform_rendering(self):
        self.screen.fill(BASE_COLOR)
        self.draw_scene()
        if self.scene.__class__.__name__ == 'GameScene':
            pass
            self.debugger.draw(info=self.content)
        # self.debugger.draw(info=self.clock.get_fps(), position=(0, 0))

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
