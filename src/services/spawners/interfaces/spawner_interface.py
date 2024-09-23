from abc import ABC, abstractmethod


class SpawnerInterface(ABC):
    @abstractmethod
    def _spawn(self):
        pass
