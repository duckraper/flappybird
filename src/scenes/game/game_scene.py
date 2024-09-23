import pygame as pg

from src.scenes.base.base_scene import BaseScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene
from src.services import GameController
from src.utils.helpers import is_pressed


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.controller = GameController(self)

    def __pause_game(self):
        self.stop_running()
        self.game.scenes_stack.push(self)
        self.game.set_scene(PauseMenuScene(game=self.game))

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        # game input
        self.controller.get_input(keydown_events)
        # quit
        if is_pressed(keydown_events, ['q', 'esc']):
            self.game.stop_running()
        # pause game
        elif is_pressed(keydown_events, 'p'):
            self.__pause_game()

    def draw(self, *args, **kwargs):
        super().draw(bg_color='sky_blue')
        self.controller.draw_all_sprites()

    def update(self, *args, **kwargs):
        self._get_input()

        if self.running:
            self.controller.update_all_sprites()
