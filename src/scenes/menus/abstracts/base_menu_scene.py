from abc import ABC
from enum import IntEnum

import pygame as pg

from src.commons.helpers import is_pressed
from src.scenes.abstracts.base_scene import BaseScene
from src.scenes.managers import MenuActionsManger

UP, DOWN = (-1, 1)


class BaseMenuScene(BaseScene,
                    ABC):
    def __init__(self, game, menu_title, captions=None, *options, **kwargs):
        super().__init__(game, vx=5, **kwargs)

        if captions is None:
            captions = []

        self.title = menu_title
        self.captions = captions
        self.options_list = IntEnum('Options', options)
        self.manager = MenuActionsManger(self, options)

        self.startup()

    def update_options_list(self):
        pass

    def draw(self, *args, **kwargs):
        super().draw()

        self.manager.draw_menu(self.game.screen,
                                title_shadow_width=5)

    def update(self, *args, **kwargs):
        super().update()
        self._get_input()

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        if is_pressed(keydown_events, 'up'):
            self.manager.update_selected_option(UP)
        elif is_pressed(keydown_events, 'down'):
            self.manager.update_selected_option(DOWN)
        elif is_pressed(keydown_events, ['enter', 'space']):
            # calls the function f'perform_{action}'
            self.manager.call_method(self.manager.selected_option_name)
