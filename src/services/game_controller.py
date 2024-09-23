from time import time

import pygame as pg

from src.core.settings import DIFFICULTY_LEVELS
from src.entities.bird import Bird
from src.services.spawners import SpawnerService
from src.utils.helpers import is_pressed
from src.mixins import CollisionDetectionMixin, SpriteManagerMixin


class GameController(SpriteManagerMixin,
                     CollisionDetectionMixin):
    def __init__(self, scene: 'BaseScene'):
        self.scene = scene

        self.spawner = SpawnerService(self)

        self.max_pipes_offset = self.get_game_prop('max_pipes_offset')
        self.min_pipes_offset = self.get_game_prop('min_pipes_offset')

        bird = self.spawner('bird')
        self.pipes = pg.sprite.Group()
        self.bird = pg.sprite.GroupSingle(bird)
        self.sprites = pg.sprite.Group([self.bird, self.pipes])

        self.game_speed = self.get_game_prop('speed')
        self.spawn_rate = self.get_game_prop('spawn_rate')
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

    def spawn_pipes(self):
        now = time()
        if now - self.last_spawn_time > self.spawn_rate:
            self.last_spawn_time = now
            pipes = self.spawner('pipe')
            print(pipes)
            self.pipes.add(pipes)

            self.sprites.add(pipes)
            print(self.sprites)

    def __get_bird_starting_coords(self):
        x = self.screen.get_width() // 6
        y = self.screen.get_height() // 2

        return x, y
