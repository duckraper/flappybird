from pygame.sprite import Sprite

from .base import BaseSpawner
from .mixins import BirdSpawnerMixin, PipeSpawnerMixin, FloorSpawnerMixin


class SpawnerService(BirdSpawnerMixin,
                     PipeSpawnerMixin,
                     FloorSpawnerMixin,
                     BaseSpawner):
    def __init__(self, controller: 'GameController'):
        super().__init__(controller)

        self.min_pipes_offset = self.controller.get_game_prop('min_pipes_offset')
        self.max_pipes_offset = self.controller.get_game_prop('max_pipes_offset')


    def __call__(self, entity_type: str) -> Sprite | list[Sprite]:
        return self.spawn(entity_type)

    def spawn(self, entity_type: str) -> Sprite | list[Sprite]:
        print(entity_type)
        if entity_type == 'bird':
            return self.spawn_bird()
        elif entity_type == 'pipe':
            return self.spawn_pipe()
        elif entity_type == 'floor':
            return self.spawn_floor()
        else:
            raise ValueError(f'Invalid entity type: {entity_type}')
