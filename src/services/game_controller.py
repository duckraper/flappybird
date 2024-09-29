import pygame as pg

from src.core.game.settings import DIFFICULTY_LEVELS
from src.core.mixins import CollisionDetectionMixin, SpriteManagerMixin, GameLogicMixin
from src.entities.spawner import EntitiySpawner
from src.utils.helpers import is_pressed


class GameController(SpriteManagerMixin,
                     CollisionDetectionMixin,
                     GameLogicMixin):
    def __init__(self, scene: 'BaseScene'):
        self.scene = scene

        self.game_speed = self.get_game_prop('speed')
        self.spawn_rate = self.get_game_prop('spawn_rate')

        self.max_pipes_offset = self.get_game_prop('max_pipes_offset')
        self.min_pipes_offset = self.get_game_prop('min_pipes_offset')

        spawn_rate = self.get_game_prop('spawn_rate')
        self.spawner = EntitiySpawner(self, spawn_rate)

        bird = self.spawner('bird')

        self.pipes = pg.sprite.Group()
        self.floor = pg.sprite.Group()
        self.bird = pg.sprite.GroupSingle(bird)
        self.sprites = pg.sprite.Group([self.floor, self.bird, self.pipes])

        self.game_over = False
        self.score = 0

    @property
    def screen(self):
        return self.scene.game.screen

    def get_game_prop(self, prop) -> int:
        return DIFFICULTY_LEVELS[self.scene.game.difficulty][prop]

    def get_input(self, keysdown):
        if not self.game_over:
            if is_pressed(keysdown, ['space', 'up', 'w']):
                if not self.scene.running:
                    self.scene.startup()
                self.bird.sprite.jump()

    def perform_game_over(self):
        pg.time.delay(1000)
        self.scene.perform_game_over()

    def spawn_sprites(self):
        self.spawner('floor')
        self.spawner('pipe')

    def update(self):
        self.spawn_sprites()
        self.update_all_sprites()
        self.handle_collisions()
        self.check_score()

    def __get_bird_starting_coords(self):
        x = self.screen.get_width() // 6
        y = self.screen.get_height() // 2

        return x, y
