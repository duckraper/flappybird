from abc import ABC
from functools import lru_cache
from typing import Union

import pygame as pg

from src.commons.helpers import get_font, get_color


class BaseTextRenderer(ABC):
    def render(
            self,
            surface: pg.Surface,
            position: Union[tuple[int, int], 'Rect'],
            text: str, **kwargs
    ) -> None:
        text_surface = self.get_surface(text, **kwargs)

        if isinstance(position, pg.Rect):
            position = position.center
        text_rect = text_surface.get_rect(center=position)

        surface.blit(text_surface, text_rect)

    def get_surface(self, text: str, **kwargs) -> pg.Surface:
        font_type = kwargs.get('font_name', 'default')
        font_size = kwargs.get('font_size', 32)
        font_color = kwargs.get('font_color', 'white')
        outline_width = kwargs.get('outline_width', 1)
        outline_color = get_color(kwargs.get('outline_color', 'black'))
        shadow_width = kwargs.get('shadow_width', 0)
        shadow_color = get_color(kwargs.get('shadow_color', 'black'))

        font = get_font(font_name=font_type, font_size=font_size)

        return self.__render_with_outline(text, font, font_color,
                                          outline_color=outline_color,
                                          outline_width=outline_width,
                                          shadow_width=shadow_width,
                                          shadow_color=shadow_color)

    @lru_cache(maxsize=128)
    def __render_with_outline(self, text, font, text_color, **kwargs) -> pg.Surface:
        outline_color = get_color(kwargs.get('outline_color'))
        outline_width = kwargs.get('outline_width')
        shadow_width = kwargs.get('shadow_width')

        text_surface = font.render(text, True, text_color)

        outline_surface = pg.Surface((text_surface.get_width() + 2 * outline_width,
                                      text_surface.get_height() + 2 * outline_width),
                                     pg.SRCALPHA)

        # render outline by blitting multiple times
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width * shadow_width + 1):
                if dx != 0 or dy != 0:  # skip center
                    outline_surface.blit(font.render(text, True, outline_color),
                                         (dx + outline_width, dy + outline_width))

        outline_surface.blit(text_surface, (outline_width, outline_width))

        return outline_surface
