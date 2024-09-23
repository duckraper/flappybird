from abc import ABC, abstractmethod

from ..interfaces import SpawnerInterface

class BaseSpawner(ABC):
    def __init__(self, controller: 'GameController'):
        self.controller = controller
