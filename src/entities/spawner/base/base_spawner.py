from abc import ABC

from src.entities.spawner.interfaces import ISpawner


class BaseSpawner(ISpawner, ABC):
    def __init__(self, controller: 'GameController'):
        self.controller = controller
