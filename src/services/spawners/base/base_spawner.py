from abc import ABC


class BaseSpawner(ABC):
    def __init__(self, controller: 'GameController'):
        self.controller = controller
