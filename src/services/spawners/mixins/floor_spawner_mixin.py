from src.core.settings import FLOOR_Y
from src.entities.floor import Floor


class FloorSpawnerMixin:
    def spawn_floor(self):
        return Floor(0, FLOOR_Y)
