import pygame as pg

from src.commons.audio_player import AudioPlayer
from src.commons.helpers import is_pressed
from src.scenes.game.renderers import ScoreRenderer
from src.scenes.abstracts.base_scene import BaseScene
from src.scenes.managers.game_flow_manager import GameFlowManager
from src.scenes.menus.game_over_menu_scene import GameOverScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.manager = GameFlowManager(self)
        self.score_render = ScoreRenderer(self)

        self.x = 0

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        self.manager.get_input(keydown_events)

        if is_pressed(keydown_events, ['p', 'esc']):
            self.pause_game()

    def pause_game(self):
        self.stop_running()
        self.game.scenes_stack.push(self)
        self.change_scene(PauseMenuScene(game=self.game))

    def stop_running(self, miliseconds=0):
        super().stop_running()
        AudioPlayer.pause_music()
        if miliseconds > 0:
            pg.time.delay(miliseconds)

    def perform_game_over(self):
        self.stop_running(300)
        self.game.set_scene(GameOverScene(game=self.game))

    def draw(self, *args, **kwargs):
        super().draw(bg_color='sky_blue')
        self.manager.draw_all_sprites()
        self.score_render()

    def update(self, *args, **kwargs):
        self.x -= 0.01
        self._get_input()

        if self.running:
            self.manager.update(kwargs.get('delta'))
