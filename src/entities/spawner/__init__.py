from time import time

from pygame.sprite import Sprite

from src.entities.spawner.base import BaseSpawner
from src.entities.spawner.mixins import BirdSpawnerMixin, PipeSpawnerMixin, FloorSpawnerMixin


class EntitiySpawner(BirdSpawnerMixin,
                     PipeSpawnerMixin,
                     FloorSpawnerMixin,
                     BaseSpawner):
    def __init__(self, manager: 'GameFlowManager', spawn_rate):
        super().__init__(manager)
        self.last_spawn_time = time()
        self.spawn_rate = spawn_rate

        self.game_speed = self.manager.game_speed

        self.min_pipes_offset = self.manager.get_game_prop('min_pipes_offset')
        self.max_pipes_offset = self.manager.get_game_prop('max_pipes_offset')

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
