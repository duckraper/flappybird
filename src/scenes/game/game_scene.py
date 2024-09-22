import pygame as pg

from src.scenes.base.base_scene import BaseScene
from src.scenes.menus.pause_menu_scene import PauseMenuScene
from src.scenes.mixins.sprites_manager_mixin import SpriteManagerMixin
from src.core.settings import DIFFICULTY_LEVELS
from src.utils.helpers import is_pressed
from src.entities.bird import Bird


class GameScene(BaseScene,
                SpriteManagerMixin):
    def __init__(self, game):
        super().__init__(game)

        self.pipes = pg.sprite.Group()
        self.bird = pg.sprite.GroupSingle(
            Bird(*self._get_bird_starting_coords()))
        self.sprites = pg.sprite.Group([self.bird, self.pipes])

        self.game_speed = self._get_game_prop('speed')
        self.spawn_rate = self._get_game_prop('spawn_rate')

    def _get_game_prop(self, prop):
        return DIFFICULTY_LEVELS[self.game.difficulty][prop]

    def _get_bird_starting_coords(self):
        return self.game.screen.get_width() // 6, self.game.screen.get_height() // 2

    def _pause_game(self):
        self.stop_running()
        self.game.scenes_stack.push(self)
        self.game.set_scene(PauseMenuScene(game=self.game))

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        # jump
        if is_pressed(keydown_events, ['space', 'up', 'w']):
            if not self.running:
                self.startup()
            self.bird.sprite.jump()
        # quit
        elif is_pressed(keydown_events, ['q', 'esc']):
            self.game.stop_running()
        # pause game
        elif is_pressed(keydown_events, 'p'):
            self._pause_game()

    def draw(self, *args, **kwargs):
        super().draw(bg_color='jasmine')
        self.draw_all_sprites()

    def update(self, *args, **kwargs):
        self._get_input()

        if self.running:
            self.update_all_sprites()
