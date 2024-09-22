from src.utils.helpers import get_font, render_text_with_outline
from src.utils.constants import DEFAULT_TITLE_FONT_SIZE, DEFAULT_TITLE_FONT_COLOR, DEFAULT_OPTION_FONT_COLOR, \
    DEFAULT_OPTION_FONT_SIZE, DEFAULT_HOVER_OPTION_FONT_COLOR, DEFAULT_HOVER_OPTION_FONT_SIZE, \
    DEFAULT_OPTIONS_OFFSET, DEFAULT_OUTLINE_WIDTH, DEFAULT_SHADOW_WIDTH, DEFAULT_OUTLINE_COLOR


class MenuRenderMixin:
    @property
    def selected_option_name(self) -> str:
        return self.menu_option(self.selected_option).name

    def draw_menu(self, screen, **kwargs):
        screen_width, screen_height = screen.get_size()

        title_font_size: int = kwargs.get('title_font_size', DEFAULT_TITLE_FONT_SIZE)
        title_font_color: str | tuple = kwargs.get('title_font_color', DEFAULT_TITLE_FONT_COLOR)
        title_outline_width: int = kwargs.get('title_outline_width', DEFAULT_OUTLINE_WIDTH)
        title_shadow_width: int = kwargs.get('title_shadow_width', DEFAULT_SHADOW_WIDTH)
        title_outline_color: str | tuple = kwargs.get('title_outline_color', DEFAULT_OUTLINE_COLOR)

        option_font_color: str | tuple = kwargs.get('option_font_color', DEFAULT_OPTION_FONT_COLOR)
        option_font_size: int = kwargs.get('option_font_size', DEFAULT_OPTION_FONT_SIZE)
        option_hover_font_color: str | tuple = kwargs.get('option_hover_font_color', DEFAULT_HOVER_OPTION_FONT_COLOR)
        option_hover_font_size: int = kwargs.get('option_hover_font_size', DEFAULT_HOVER_OPTION_FONT_SIZE)
        options_offset: int = kwargs.get('options_offset', DEFAULT_OPTIONS_OFFSET)
        option_outline_width: int = kwargs.get('option_outline_width', DEFAULT_OUTLINE_WIDTH)
        option_shadow_width: int = kwargs.get('option_shadow_width', DEFAULT_SHADOW_WIDTH)
        option_outline_color: str | tuple = kwargs.get('option_outline_color', DEFAULT_OUTLINE_COLOR)

        self._draw_title(screen, screen_width, screen_height, title_font_size, title_font_color, title_outline_width, title_shadow_width, title_outline_color)
        self._draw_options(screen, screen_width, screen_height, option_font_color, option_font_size, option_hover_font_color, option_hover_font_size, options_offset, option_outline_width, option_shadow_width, option_outline_color)

    def _draw_title(self, screen, screen_width, screen_height, font_size, font_color, outline_width, shadow_width, outline_color):
        title_surface = self._create_font_surface(self.menu_title, font_size, font_color, outline_width, shadow_width, outline_color)
        title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(title_surface, title_rect)

    def _draw_options(self, screen, screen_width, screen_height, font_color, font_size, hover_font_color, hover_font_size, options_offset, outline_width, shadow_width, outline_color):
        for option_index in self.menu_option:
            option_color, option_font_size = (hover_font_color, hover_font_size) if option_index == self.selected_option else (font_color, font_size)
            option_text = self._create_font_surface(option_index.name, option_font_size, option_color, outline_width, shadow_width, outline_color)
            x = screen_width // 2
            y = screen_height // 2.5 + option_index.value * options_offset
            option_rect = option_text.get_rect(center=(x, y))
            screen.blit(option_text, option_rect)

    @staticmethod
    def _create_font_surface(text, font_size, color, outline_width, shadow_width, outline_color):
        font = get_font(font_size=font_size)
        return render_text_with_outline(text, font, color, outline_width=outline_width, shadow_width=shadow_width, outline_color=outline_color)

    def update_selected_option(self, direction):
        self.selected_option = (((self.selected_option + direction - 1) % len(self.menu_option)) + 1)