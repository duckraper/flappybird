from abc import ABC
from enum import IntEnum

import pygame as pg

from src.commons.helpers import is_pressed
from src.scenes.abstracts.base_scene import BaseScene
from src.scenes.menus.mixins import MenuActionHandlerMixin, MenuRenderMixin

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
        super().draw(bg='sky_blue')

        self.draw_menu(self.game.screen, title_shadow_width=5)

    def update(self, *args, **kwargs):
        self._get_input()

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        if is_pressed(keydown_events, 'up'):
            self.update_selected_option(UP)
        elif is_pressed(keydown_events, 'down'):
            self.update_selected_option(DOWN)
        elif is_pressed(keydown_events, ['enter', 'space']):
            # calls the function f'perform_{action}'
            self.call_method(self.selected_option_name)
