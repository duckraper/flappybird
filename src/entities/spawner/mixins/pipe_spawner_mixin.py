import os
import random as r

from time import time

from src.commons.constants import INGAME_DEADZONE
from src.commons.helpers import is_between
from src.core.game.settings import SCREEN_WIDTH
from src.entities.sprites.pipe import Pipe
from src.resources.spritesheets import pipe_spritesheet


class PipeSpawnerMixin:
    def spawn_pipe(self):
        now = time()
        last_pipe = self.manager.pipes.sprites()[-1] if self.manager.pipes else None

        if last_pipe:
            last_pipe_x = last_pipe.rect.right
        else:
            last_pipe_x = 0

        if now - self.last_spawn_time > self.spawn_rate \
                and SCREEN_WIDTH - last_pipe_x > self.pipes_x_offset:
            pipes = self.create_pipes()

            if pipes:
                self.manager.pipes.add(pipes)
                self.manager.sprites.add(pipes, layer=2)

                self.last_spawn_time = now

            return pipes

    def create_pipes(self):
        x, y = self._get_central_coords()
        offset = self.pipes_offset

        y_upside_down = y - offset
        y_normal = y + offset

        if self.is_placed_out_of_deadzone(y_upside_down, y_normal):
            return self.spawn_pipe()

        speed = self.manager.game_speed
        color = r.choice(list(pipe_spritesheet.keys()))

        return [
                Pipe(x, y_upside_down, color, upside_down=True, speed=speed),
                Pipe(x, y_normal, color, upside_down=False, speed=speed)
            ]

    @property
    def pipes_offset(self) -> int:
        return r.randint(self.min_pipes_y_offset, self.max_pipes_y_offset) // 2

    @staticmethod
    def is_placed_out_of_deadzone(*y_positions) -> bool:
        return not all(
            is_between(y, INGAME_DEADZONE[0], INGAME_DEADZONE[1])
            for y in y_positions
        )

    @staticmethod
    def _get_central_coords() -> tuple[int, int]:
        x = SCREEN_WIDTH
        y = r.randint(*INGAME_DEADZONE)

        return x, y
