from abc import ABC

from ..interfaces import IMenuComponent


class MenuComponent(ABC):
    def __init__(self, name):
        self.name = name
