from abc import ABC, abstractmethod


class IMenuComponent(ABC):
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass
