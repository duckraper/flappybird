from src.scenes.game.game_scene import GameScene
from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class MainMenuScene(BaseMenuScene):
    def __init__(self, game):
        options_list = [
            "Start",
            "Settings",
            "High Scores",
            "Quit"
        ]
        super().__init__(game, game.title, *options_list)

    def draw(self, *args, **kwargs):
        super().draw(title_font_size=180)

    def perform_start(self):
        self.game.set_scene(GameScene(game=self.game))

    def perform_high_scores(self):
        from .high_scores_scene import HighScoresScene

        self.game.set_scene(HighScoresScene(game=self.game))

    def perform_settings(self):
        from .settings_menu_scene import SettingsScene

        self.game.set_scene(SettingsScene(game=self.game))

    def perform_quit(self):
        self.game.stop_running()
