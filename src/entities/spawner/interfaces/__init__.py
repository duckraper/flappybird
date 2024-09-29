from abc import ABC, abstractmethod


class ISpawner(ABC):
    @abstractmethod
    def spawn(self, entity_type: str):
        pass
