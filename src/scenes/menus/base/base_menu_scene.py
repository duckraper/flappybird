from abc import ABC
from enum import IntEnum, Enum

import pygame as pg

from src.scenes.menus.mixins import MenuActionHandlerMixin, MenuRenderMixin
from src.utils.helpers import is_pressed, get_font, get_color, render_text_with_outline
from src.scenes.base.base_scene import BaseScene
from src.utils.constants import DEFAULT_TITLE_FONT_SIZE, DEFAULT_TITLE_FONT_COLOR, DEFAULT_OPTION_FONT_COLOR, \
    DEFAULT_OPTION_FONT_SIZE, DEFAULT_HOVER_OPTION_FONT_COLOR, DEFAULT_HOVER_OPTION_FONT_SIZE, \
    DEFAULT_OPTIONS_OFFSET, DEFAULT_OUTLINE_WIDTH, DEFAULT_SHADOW_WIDTH, DEFAULT_OUTLINE_COLOR

UP, DOWN = (-1, 1)


class BaseMenuScene(BaseScene,
                    MenuActionHandlerMixin,
                    MenuRenderMixin,
                    ABC):
    def __init__(self, game, menu_title, *options):
        super().__init__(game)

        self.menu_title = menu_title
        self.menu_option = IntEnum('Option', options)
        self.selected_option = 1

        self.startup()

    def draw(self, *args, **kwargs):
        super().draw(bg_color='sky_blue')

        self.draw_menu(self.game.screen, title_shadow_width=5)

    def update(self):
        self._get_input()

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        if is_pressed(keydown_events, 'up'):
            self.update_selected_option(UP)
        elif is_pressed(keydown_events, 'down'):
            self.update_selected_option(DOWN)
        elif is_pressed(keydown_events, 'enter'):
            # calls the function f'perform_{action}'
            self.call_method(self.selected_option_name)
