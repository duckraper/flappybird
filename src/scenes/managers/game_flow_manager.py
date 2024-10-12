from random import choice

import pygame as pg

from src.commons.audio_player import AudioPlayer
from src.commons.constants import BG_SPEED
from src.commons.decorators import has_sfx
from src.commons.helpers import is_pressed
from src.core.game.settings import DIFFICULTY_LEVELS, DIE_VOLUME
from src.core.physics import Physics
from src.entities.spawner import EntitiySpawner
from src.entities.sprites.background import Background
from src.resources.backgrounds import backgrounds
from src.scenes.managers.mixins import SpriteManagerMixin, CollisionDetectionMixin, GameLogicMixin


class GameFlowManager(SpriteManagerMixin,
                      CollisionDetectionMixin,
                      GameLogicMixin):
    def __init__(self, scene: 'BaseScene'):
        self.scene = scene
        self.physics = Physics()

        self.score_manager = self.scene.game.score_manager


        self.game_speed = self.get_game_prop('speed')
        self.spawn_rate = self.get_game_prop('spawn_rate')
        self.difficulty = self.scene.game.difficulty
        
        self.hardened_value = 0

        self.max_pipes_offset = self.get_game_prop('max_pipes_y_offset')
        self.min_pipes_offset = self.get_game_prop('min_pipes_y_offset')
        self.pipes_x_offset = self.get_game_prop('pipes_x_offset')

        self.waiting_time = 1

        spawn_rate = self.get_game_prop('spawn_rate')
        self.spawner = EntitiySpawner(self, spawn_rate)

        bird = self.spawner('bird')

        self.pipes = pg.sprite.Group()
        self.floor = pg.sprite.Group()
        self.bird = pg.sprite.GroupSingle(bird)
        self.background = Background(image=choice(backgrounds).copy(),
                                     vx=BG_SPEED)

        self.sprites = pg.sprite.LayeredUpdates()

        self.sprites.add(self.background, layer=0)
        self.sprites.add(self.bird, layer=1)
        self.sprites.add(self.pipes, layer=2)
        self.sprites.add(self.floor, layer=3)

        self.game_over = False
        self.score = 0

        self.spawner.spawn_floor()

        self.sprites.update(self.scene.game.get_delta())

    @property
    def screen(self):
        return self.scene.game.screen

    def set_spawn_rate(self, spawn_rate):
        self.spawn_rate = spawn_rate
        self.spawner.set_spawn_rate(spawn_rate)

    def set_game_speed(self, game_speed):
        self.game_speed = game_speed

    def get_game_prop(self, prop) -> int:
        return DIFFICULTY_LEVELS[self.scene.game.difficulty][prop]

    def get_input(self, keysdown):
        if self.game_over:
            return
        if is_pressed(keysdown, 'any'):
            if not self.scene.running:
                if not hasattr(self, 'started'):
                    self.start_game()
                else:
                    self.resume_game()

        if is_pressed(keysdown, ['space', 'up', 'w']):
            self.bird.sprite.jump(self.scene.game.get_delta())

    def start_game(self):
        self.started = True

        AudioPlayer.set_music()
        AudioPlayer.play_music(loops=1)
        self.scene.startup()

    def resume_game(self):
        AudioPlayer.resume_music()
        self.scene.running = True

    @has_sfx('die', DIE_VOLUME)
    def perform_game_over(self):
        AudioPlayer.stop_music()
        self.score_manager.save_score(self.score)
        self.scene.perform_game_over()

    def update(self, delta):
        if not self.scene.running:
            return

        if not self.game_over:
            self.check_score()
            self.spawn_sprites()

        self.handle_collisions()
        self.check_game_over()
        self.physics.apply_gravity(self.sprites, delta)
        self.update_all_sprites()

    def __get_bird_starting_coords(self):
        x = self.screen.get_width() // 6
        y = self.screen.get_height() // 2

        return x, y
