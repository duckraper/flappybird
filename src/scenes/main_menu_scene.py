from .base_menu_scene import BaseMenuScene
from .game_scene import GameScene


class MainMenuScene(BaseMenuScene):
    def __init__(self, game):
        options_list = [
            "Start",
            "Settings",
            "High Scores",
            "Quit"
        ]
        super().__init__(game, game.title, *options_list)

    def draw(self):
        screen = self.game.screen
        screen_width, screen_height = screen.get_size()

        self._draw_title(screen, screen_width, screen_height)
        self._draw_options(screen, screen_width, screen_height)

    def _draw_title(self, screen, screen_width, screen_height):
        title_surface = self.get_title_font_surface(75)
        title_rect = title_surface.get_rect(center=self._title_axis(screen_width, screen_height))
        screen.blit(title_surface, title_rect)

    def _title_axis(self, screen_width, screen_height) -> tuple[int, int]:
        title_x = screen_width // 2
        title_y = screen_height // 4

        return title_x, title_y

    def _draw_options(self, screen, screen_width, screen_height):
        for option_index in self.menu_option:
            option_color, option_font_size = self._get_option_style(option_index)
            option_text = self.get_option_font_surface_by_index(index=option_index,
                                                                color=option_color,
                                                                font_size=option_font_size)
            option_rect = option_text.get_rect(
                center=(screen_width // 2, screen_height // 2.5 + option_index * 60)
            )
            screen.blit(option_text, option_rect)

    def _get_option_style(self, option_index):
        if option_index == self.selected_option:
            option_color = 'black'
            option_font_size = 34
        else:
            option_color = 'less_black'
            option_font_size = 30

        return option_color, option_font_size

    def perform_start(self):
        self.game.set_scene(GameScene(game=self.game))

    def perform_high_scores(self):
        raise NotImplementedError

    def perform_settings(self):
        raise NotImplementedError

    def perform_quit(self):
        self.game.stop_running()
