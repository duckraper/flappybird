from abc import ABC, abstractmethod


class BaseScene(ABC):
    def __init__(self, game):
        self.running = False
        self.game = game

    def stop_running(self):
        self.running = False

    def startup(self):
        self.running = True

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass
