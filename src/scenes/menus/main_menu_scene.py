from enum import IntEnum

from src.core.game.settings import DIFFICULTY_LEVELS
from src.scenes.game.game_scene import GameScene
from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class MainMenuScene(BaseMenuScene):
    def __init__(self, game, **kwargs):
        options_list = [
            "Start",
            "Difficulty: {i}",
            "High Scores",
            "Quit"
        ]
        super().__init__(game, game.title, None,*options_list, **kwargs)
        self.update_options_list()

    def startup(self):
        super().startup()

    def draw(self, *args, **kwargs):
        super().draw(title_font_size=200)

    def update_options_list(self):
        self.options_list = [
            "Start",
            f"Difficulty: {self.game.difficulty.title()}",
            "High Scores",
            "Quit"
        ]
        self.manager.menu_option = IntEnum('Option', self.options_list)

    def perform_start(self):
        self.game.scenes_stack.push(self)
        self.change_scene(GameScene(game=self.game))

    def perform_difficulty(self):
        difficulties = list(DIFFICULTY_LEVELS.keys())
        current_index = difficulties.index(self.game.difficulty)
        new_index = (current_index + 1) % len(difficulties)
        self.game.set_difficulty(difficulties[new_index])

    def perform_high_scores(self):
        from .high_scores_scene import HighScoresScene

        self.game.scenes_stack.push(self)
        self.change_scene(HighScoresScene(game=self.game, background=self.background.copy()))

    def perform_quit(self):
        self.game.stop_running()
