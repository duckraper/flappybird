from abc import ABC
from enum import IntEnum, Enum

import pygame as pg

from src.scenes.mixins import MenuActionHandlerMixin
from src.utils.helpers import is_pressed, get_font, get_color, render_text_with_outline
from .base_scene import BaseScene
from src.utils.constants import DEFAULT_TITLE_FONT_SIZE, DEFAULT_TITLE_FONT_COLOR, DEFAULT_OPTION_FONT_COLOR, \
    DEFAULT_OPTION_FONT_SIZE, DEFAULT_HOVER_OPTION_FONT_COLOR, DEFAULT_HOVER_OPTION_FONT_SIZE, \
    DEFAULT_OPTIONS_OFFSET, DEFAULT_OUTLINE_WIDTH, DEFAULT_SHADOW_WIDTH, DEFAULT_OUTLINE_COLOR

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

    def draw(self, *args, **kwargs):
        super().draw(bg_color='sky_blue')
        
        screen = self.game.screen
        screen_width, screen_height = screen.get_size()

        title_font_size: int = kwargs.get('title_font_size', DEFAULT_TITLE_FONT_SIZE)
        title_font_color: str | tuple = kwargs.get('title_font_color', DEFAULT_TITLE_FONT_COLOR)
        option_font_color: str | tuple = kwargs.get('option_font_color', DEFAULT_OPTION_FONT_COLOR)
        option_font_size: int = kwargs.get('option_font_size', DEFAULT_OPTION_FONT_SIZE)
        option_hover_font_color: str | tuple = kwargs.get('option_hover_font_color', DEFAULT_HOVER_OPTION_FONT_COLOR)
        option_hover_font_size: int = kwargs.get('option_hover_font_size', DEFAULT_HOVER_OPTION_FONT_SIZE)
        options_offset: int = kwargs.get('options_offset', DEFAULT_OPTIONS_OFFSET)
        outline_width: int = kwargs.get('outline_width', DEFAULT_OUTLINE_WIDTH)
        shadow_width: int = kwargs.get('shadow_width', DEFAULT_SHADOW_WIDTH)
        outline_color: str | tuple = kwargs.get('outline_color', DEFAULT_OUTLINE_COLOR)

        self._draw_title(
            screen,
            screen_width,
            screen_height,
            font_color=title_font_color,
            font_size=title_font_size,
            outline_width=outline_width,
            shadow_width=shadow_width + 2,
            outline_color=outline_color
        )

        self._draw_options(
            screen,
            screen_width,
            screen_height,
            font_color=option_font_color,
            font_size=option_font_size,
            hover_font_color=option_hover_font_color,
            hover_font_size=option_hover_font_size,
            options_offset=options_offset,
            outline_width=outline_width,
            shadow_width=shadow_width,
            outline_color=outline_color
        )

    def _draw_title(self, screen, screen_width, screen_height, **kwargs):
        font_color = kwargs.get('font_color')
        font_size = kwargs.get('font_size')
        outline_width = kwargs.get('outline_width')
        shadow_width = kwargs.get('shadow_width')
        outline_color = kwargs.get('outline_color')

        title_surface = self._get_title_font_surface(
             font_size,
             font_color,
             outline_width=outline_width,
             shadow_width=shadow_width,
             outline_color=outline_color
        )
        title_rect = title_surface.get_rect(center=self._get_title_axis(screen_width, screen_height))
        screen.blit(title_surface, title_rect)

    def _draw_options(self, screen, screen_width, screen_height, **kwargs):
        font_color = kwargs.get('font_color')
        font_size = kwargs.get('font_size')
        hover_font_color = kwargs.get('hover_font_color')
        hover_font_size = kwargs.get('hover_font_size')
        options_offset = kwargs.get('options_offset')
        outline_width = kwargs.get('outline_width')
        shadow_width = kwargs.get('shadow_width')
        outline_color = kwargs.get('outline_color')

        for option_index in self.menu_option:
            option_color, option_font_size = self._get_option_style(
                 option_index,
                 font_color=font_color,
                 font_size=font_size,
                 hover_font_color=hover_font_color,
                 hover_font_size=hover_font_size,
            )
            option_text = self._get_option_font_surface_by_index(
                 index=option_index,
                 color=option_color,
                 font_size=option_font_size,
                 outline_width=outline_width,
                 shadow_width=shadow_width,
                 outline_color=outline_color
            )
            x = screen_width // 2
            y = screen_height // 2.5 + option_index.value * options_offset
            option_rect = option_text.get_rect(
                center=(x, y)
            )
            screen.blit(option_text, option_rect)

    def _get_title_font_surface(
            self, font_size: int, color: str | tuple, **kwargs) -> pg.surface.Surface:
        outline_width = kwargs.get('outline_width')
        shadow_width = kwargs.get('shadow_width')
        outline_color = kwargs.get('outline_color')

        return self._create_font_surface(
            self.menu_title,
            font_size,
            color,
            outline_width=outline_width,
            shadow_width=shadow_width,
            outline_color=outline_color
        )

    @staticmethod
    def _create_font_surface(
            text: str, font_size: int, color: tuple, **kwargs) -> pg.surface.Surface:
        outline_width = kwargs.get('outline_width')
        shadow_width = kwargs.get('shadow_width')
        outline_color = kwargs.get('outline_color')

        font: pg.font.Font = get_font(font_size=font_size)

        return render_text_with_outline(
            text,
            font,
            color,
            outline_width=outline_width,
            shadow_width=shadow_width,
            outline_color=outline_color
        )

    @staticmethod
    def _get_title_axis(screen_width, screen_height) -> tuple[int, int]:
        title_x = screen_width // 2
        title_y = screen_height // 4

        return title_x, title_y

    def _get_option_style(self, index, **kwargs) -> tuple:
        if index == self.selected_option:
            option_color = kwargs.get('hover_font_color')
            option_font_size = kwargs.get('hover_font_size')
        else:
            option_color = kwargs.get('font_color')
            option_font_size = kwargs.get('font_size')

        return option_color, option_font_size

    def _get_option_font_surface_by_index(
            self, index: Enum, color: str | tuple, font_size: int, **kwargs) -> 'Surface':
        outline_width = kwargs.get('outline_width')
        shadow_width = kwargs.get('shadow_width')
        outline_color = kwargs.get('outline_color')

        font_color = get_color(color)

        return self._create_font_surface(
            index.name,
            font_size,
            font_color,
            outline_width=outline_width,
            shadow_width=shadow_width,
            outline_color=outline_color
        )

    def _update_selected_option(self, direction: int):
        self.selected_option = (((self.selected_option + direction - 1)
                                 % len(self.menu_option))
                                + 1)

    def update(self):
        self._get_input()

    def _get_input(self):
        keydown_events = pg.event.get(eventtype=(pg.KEYDOWN,))

        if is_pressed(keydown_events, 'up'):
            self._update_selected_option(UP)
        elif is_pressed(keydown_events, 'down'):
            self._update_selected_option(DOWN)
        elif is_pressed(keydown_events, 'enter'):
            # calls the function f'perform_{action}'
            self.call_method(self.selected_option_name)
