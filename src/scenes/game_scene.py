import pygame as pg

from . import BaseScene
from ..core.mixins import SpriteManagerMixin
from ..core.settings import DIFFICULTY_LEVELS
from ..utils.helpers import is_pressed
from ..entities.bird import Bird


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

    def get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        if is_pressed(keydown_events, ['space', 'up', 'w']):
            if not self.running:
                self.startup()
            self.bird.sprite.jump()

    def draw(self, *args, **kwargs):
        self.draw_all_sprites()

    def update(self, *args, **kwargs):
        self.get_input()

        if self.running:
            self.update_all_sprites()


