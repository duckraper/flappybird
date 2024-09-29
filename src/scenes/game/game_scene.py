import pygame as pg

from src.scenes.abstracts.base_scene import BaseScene
from src.scenes.menus.game_over_menu_scene import GameOverScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene
from src.services import GameController
from src.utils.helpers import is_pressed


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.controller = GameController(self)
        self.controller.spawner.spawn_floor()


    def __pause_game(self):
        self.stop_running()
        self.game.scenes_stack.push(self)
        self.game.set_scene(PauseMenuScene(game=self.game))

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        # game input
        self.controller.get_input(keydown_events)
        # # quit
        # if is_pressed(keydown_events, ['q']):
        #     self.game.stop_running()
        # pause game
        if is_pressed(keydown_events, ['p', 'esc']):
            self.__pause_game()

    def perform_game_over(self):
        self.stop_running()
        self.game.set_scene(GameOverScene(game=self.game))

    def draw(self, *args, **kwargs):
        super().draw(bg_color='sky_blue')
        self.controller.draw_all_sprites()

    def update(self, *args, **kwargs):
        self._get_input()

        if self.running:
            self.controller.update()
