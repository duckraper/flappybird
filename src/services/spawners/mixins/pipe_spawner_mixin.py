import random as r

from src.entities.pipe import Pipe
from src.core.settings import SCREEN_WIDTH, SCREEN_HEIGHT, INGAME_DEADZONE
from src.utils.helpers import is_between, placed_out_of_deadzone


class PipeSpawnerMixin:
    def spawn_pipe(self):
        x, y = self._get_central_coords()
        offset = self.pipes_offset

        y_upside_down = y - offset
        y_normal = y + offset

        if placed_out_of_deadzone(y_upside_down, y_normal):
            return self.spawn_pipe()

        upper_pipe = Pipe(x, y_upside_down, upside_down=True)
        bottom_pipe = Pipe(x, y_normal, upside_down=False)

        return [upper_pipe, bottom_pipe]

    @property
    def pipes_offset(self) -> int:
        return r.randint(self.min_pipes_offset, self.max_pipes_offset) // 2

    @staticmethod
    def _get_central_coords() -> tuple[int, int]:
        x = SCREEN_WIDTH + 40
        y = r.randint(*INGAME_DEADZONE)

        return x, y
