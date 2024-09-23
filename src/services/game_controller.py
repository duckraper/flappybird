from time import time

import pygame as pg

from src.core.settings import DIFFICULTY_LEVELS
from src.entities.bird import Bird
from src.services.spawners import SpawnerService
from src.utils.helpers import is_pressed
from src.mixins import CollisionDetectionMixin, SpriteManagerMixin, GameLogicMixin


class GameController(SpriteManagerMixin,
                     CollisionDetectionMixin,
                     GameLogicMixin):
    def __init__(self, scene: 'BaseScene'):
        self.scene = scene

        self.spawner = SpawnerService(self)

        self.game_speed = self.get_game_prop('speed')
        self.spawn_rate = self.get_game_prop('spawn_rate')

        self.max_pipes_offset = self.get_game_prop('max_pipes_offset')
        self.min_pipes_offset = self.get_game_prop('min_pipes_offset')

        floor = self.spawner('floor')
        bird = self.spawner('bird')

        self.pipes = pg.sprite.Group()
        self.floor = pg.sprite.GroupSingle(floor)
        self.bird = pg.sprite.GroupSingle(bird)
        self.sprites = pg.sprite.Group([self.floor, self.bird, self.pipes])

        self.score = 0

        self.last_spawn_time = time()

    @property
    def screen(self):
        return self.scene.game.screen

    def get_game_prop(self, prop) -> int:
        return DIFFICULTY_LEVELS[self.scene.game.difficulty][prop]

    def get_input(self, keysdown):
        if is_pressed(keysdown, ['space', 'up', 'w']):
            if not self.scene.running:
                self.scene.startup()
            self.bird.sprite.jump()

    def update(self):
        self.update_all_sprites()
        self.check_collisions()
        self.check_score()

    def __get_bird_starting_coords(self):
        x = self.screen.get_width() // 6
        y = self.screen.get_height() // 2

        return x, y
