from abc import ABC
from enum import IntEnum, Enum

import pygame as pg

from src.core.mixins import MenuActionHandlerMixin
from src.utils.helpers import is_pressed, get_font
from . import BaseScene
from ..utils import COLORS

UP, DOWN = (-1, 1)


class BaseMenuScene(BaseScene,
                    MenuActionHandlerMixin,
                    ABC):
    def __init__(self, game, menu_title, *options):
        super().__init__(game)

        self.menu_title = menu_title
        self.menu_option = IntEnum('Option', options)
        self.selected_option = 1

        self.startup()

    @property
    def selected_option_name(self) -> str:
        return self.menu_option(self.selected_option).name


    def get_title_font_surface(self, font_size=70) -> pg.surface.Surface:
        return self._create_font_surface(
            self.menu_title, font_size, COLORS['black']
        )

    @staticmethod
    def _create_font_surface(
            text: str, font_size: int, color: tuple) -> pg.surface.Surface:
        font: pg.font.Font = get_font(font_size=font_size)
        return font.render(text, True, color)

    def get_option_font_surface_by_index(
            self, index: Enum, color: str | tuple = 'black', font_size: int = 30) -> pg.surface.Surface:
        if isinstance(color, str):
            try:
                color = COLORS[color]
            except KeyError:
                raise ValueError(f'Color {color} not found in COLORS')

        return self._create_font_surface(
            index.name, font_size, color
        )

    def _update_selected_option(self, direction: int):
        self.selected_option = (((self.selected_option + direction - 1)
                                 % len(self.menu_option))
                                + 1)

    def update(self):
        self.get_input()

    def get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        if is_pressed(keydown_events, 'up'):
            self._update_selected_option(UP)
        elif is_pressed(keydown_events, 'down'):
            self._update_selected_option(DOWN)
        elif is_pressed(keydown_events, 'enter'):
            # calls the function f'perform_{action}'
            self.call_method(self.selected_option_name)
