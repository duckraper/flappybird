import time

from src.commons.audio_player import AudioPlayer
from src.commons.helpers import get_color
from src.core.game.settings import SCORE_VOLUME, HIT_VOLUME, DIE_VOLUME
from src.commons.decorators import has_sfx
from src.entities import Pipe
from src.entities.sprites import Bird
from src.entities.sprites.abstracts import MovingSprite
from src.entities.sprites.blink import Blink


class GameLogicMixin:
    waiting_time = 1
    last_hardened_score = 0

    @has_sfx('score', SCORE_VOLUME)
    def perform_score(self, pipe: 'Pipe'):
        self.score += 1
        pipe.scored = True

    def check_score(self):
        if self.pipes.sprites():
            pipe = self.pipes.sprites()[0]
            if not hasattr(pipe, 'scored') or not pipe.scored:
                if self.bird.sprite.rect.left > pipe.rect.right:
                    self.perform_score(pipe)
                if self.score % 5 == 0 and self.score != 0 and self.score != self.last_hardened_score:
                    self.harden_game()
                    self.last_hardened_score = self.score

    def harden_game(self):
        self.set_game_speed(self.game_speed + (self.game_speed / 12))
        self.set_spawn_rate(self.spawn_rate - (self.spawn_rate / 10))

        self.physics.gravity += self.physics.gravity * 0.05

        self.max_pipes_offset -= self.max_pipes_offset * 0.05
        self.min_pipes_offset -= self.min_pipes_offset * 0.05

        for pipe in self.pipes:
            pipe.vx += pipe.vx * 0.05

    def handle_collisions(self):
        bird = self.bird.sprite
        if self.collided(bird, self.floor):
           self.handle_floor_collision(self.floor)

        collided_pipes = self.collided_with(bird, self.pipes)

        for pipe in collided_pipes:
            if not hasattr(bird, 'collided'):
                bird.collided = True
                self.handle_pipe_collision(pipe)

    @has_sfx('die', DIE_VOLUME)
    def handle_floor_collision(self, collided_floor):
        self.perform_game_over()

    @has_sfx('hit', HIT_VOLUME)
    def handle_pipe_collision(self, collided_pipe: 'Pipe'):
        self.sprites.add(Blink(get_color('red'), duration=0.1), layer=1)

        for sprite in self.sprites.sprites():
            if isinstance(sprite, MovingSprite):
                if isinstance(sprite, Bird):
                    sprite.set_speed(vx=-collided_pipe.vx)
                    continue
                sprite.set_moving(False)
        self.game_over = True