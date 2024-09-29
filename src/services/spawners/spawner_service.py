from time import time

from pygame.sprite import Sprite

from .base import BaseSpawner
from .mixins import BirdSpawnerMixin, PipeSpawnerMixin, FloorSpawnerMixin


class SpawnerService(BirdSpawnerMixin,
                     PipeSpawnerMixin,
                     FloorSpawnerMixin,
                     BaseSpawner):
    def __init__(self, controller: 'GameController', spawn_rate):
        super().__init__(controller)
        self.last_spawn_time = time()
        self.spawn_rate = spawn_rate

        self.game_speed = self.controller.game_speed

        self.min_pipes_offset = self.controller.get_game_prop('min_pipes_offset')
        self.max_pipes_offset = self.controller.get_game_prop('max_pipes_offset')

    def __call__(self, entity_type: str) -> Sprite | list[Sprite]:
        return self.spawn(entity_type)

    def spawn(self, entity_type: str) -> Sprite | list[Sprite]:
        spawn_method = f'spawn_{entity_type}'

        if hasattr(self, spawn_method):
            try:
                return getattr(self, spawn_method)()
            except Exception as e:
                raise e

        raise AttributeError(f'No method found for {entity_type}')
