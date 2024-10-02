from abc import ABC


class MenuComponent(ABC):
    def __init__(self, name):
        self.name = name
