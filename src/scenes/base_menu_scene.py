import pygame as pg
from enum import IntEnum

from src.core.mixins import MenuActionHandlerMixin
from src.utils.helpers import is_pressed, get_font
from . import BaseScene
from ..utils import COLORS


class BaseMenuScene(BaseScene, MenuActionHandlerMixin):
    def __init__(self, game, menu_title, *options):
        super().__init__(game)

        self.menu_title = menu_title
        self.menu_option = IntEnum('Option', options)
        self.selected_option = 1

    @property
    def selected_option_name(self) -> str:
        return self.menu_option(self.selected_option).name

    @property
    def title_font_surface(self) -> pg.surface.Surface:
        return self._create_font_surface(
            self.menu_title, 70, COLORS['black']
        )

    @property
    def option_font_surface(self) -> pg.surface.Surface:
        return self._create_font_surface(
            self.selected_option_name, 30, COLORS['black']
        )

    @staticmethod
    def _create_font_surface(
            text: str, font_size: int, color: tuple) -> pg.surface.Surface:
        font: pg.font.Font = get_font(font_size=font_size)
        return font.render(text, True, color)

    def get_input(self):
        update_selected_option = lambda x: (((self.selected_option + x)
                                             % len(self.menu_option))
                                             + 1)
        if is_pressed('up'):
            self.selected_option = update_selected_option(-1)
        elif is_pressed('down'):
            self.selected_option = update_selected_option(1)
        elif is_pressed('enter'):
            # calls the function f'perform_{action}'
            self.call_method(self.selected_option_name.lower())

