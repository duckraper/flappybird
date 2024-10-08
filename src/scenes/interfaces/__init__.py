from abc import ABC, abstractmethod


class IScene(ABC):
    @abstractmethod
    def change_scene(self, scene: 'Scene'):
        pass

    @abstractmethod
    def _get_input(self, *args, **kwargs):
        pass

    @abstractmethod
    def draw(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
