import random as r
from time import time

from src.core.settings import SCREEN_WIDTH, INGAME_DEADZONE
from src.entities.pipe import Pipe
from src.utils.helpers import placed_out_of_deadzone


class PipeSpawnerMixin:
    def spawn_pipe(self):
        now = time()
        if now - self.last_spawn_time > self.spawn_rate:
            pipes = self.create_pipes()

            if pipes:
                self.controller.pipes.add(pipes)
                self.controller.sprites.add(pipes)

                self.last_spawn_time = now

            return pipes

    def create_pipes(self):
        x, y = self._get_central_coords()
        offset = self.pipes_offset

        y_upside_down = y - offset
        y_normal = y + offset

        if placed_out_of_deadzone(y_upside_down, y_normal):
            return self.spawn_pipe()

        pipe_color = r.choice(['orange', 'green'])
        speed = self.controller.game_speed
        upper_pipe = Pipe(x, y_upside_down, pipe_color, upside_down=True, speed=speed)
        bottom_pipe = Pipe(x, y_normal, pipe_color, upside_down=False, speed=speed)

        return [upper_pipe, bottom_pipe]

    @property
    def pipes_offset(self) -> int:
        return r.randint(self.min_pipes_offset, self.max_pipes_offset) // 2

    @staticmethod
    def _get_central_coords() -> tuple[int, int]:
        x = SCREEN_WIDTH + 40
        y = r.randint(*INGAME_DEADZONE)

        return x, y
