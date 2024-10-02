import pygame as pg
import random as r

from src.commons.assets_loader import AssetsLoader, ASSETS_DIR
from src.commons.helpers import is_pressed
from src.commons.renderers import ScoreRenderer
from src.core.game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_SIZE
from src.entities.sprites.background import Background
from src.scenes.abstracts.base_scene import BaseScene
from src.scenes.managers.game_flow_manager import GameFlowManager
from src.scenes.menus.game_over_menu_scene import GameOverScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene
from src.resources.backgrounds import backgrounds


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.manager = GameFlowManager(self)
        self.score_render = ScoreRenderer(self)


        self.x = 0

    # def __get_background(self):
    #     bg = r.choice(backgrounds).copy()
    #     t = pg.Surface(bg.get_size(), pg.SRCALPHA)
    #     t.fill((0,0,0,10), special_flags=pg.BLEND_RGBA_MULT)
    #     bg.blit(t, (0,0))
    #     return bg

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        self.manager.get_input(keydown_events)

        if is_pressed(keydown_events, ['p', 'esc']):
            self.pause_game()

    def pause_game(self):
        self.stop_running()
        self.game.scenes_stack.push(self)
        self.game.set_scene(PauseMenuScene(game=self.game))

    def stop_running(self, miliseconds=0):
        super().stop_running()
        if miliseconds > 0:
            pg.time.delay(miliseconds)

    def perform_game_over(self):
        self.stop_running(300)
        self.game.set_scene(GameOverScene(game=self.game))

    def draw(self, *args, **kwargs):
        super().draw(bg_color='sky_blue')
        # self.game.screen.blit(self.background, (self.x,0))
        # self.game.screen.blit(self.background, (self.x+SCREEN_WIDTH,0))
        self.manager.draw_all_sprites()
        self.score_render()
        # transparency_surface = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
        # transparency_surface.fill((0, 0, 0, 180))
        # self.game.screen.blit(transparency_surface, (0, 0))

    def update(self, *args, **kwargs):
        self.x -= 0.01
        self._get_input()

        if self.running:
            self.manager.update(kwargs.get('delta'))
