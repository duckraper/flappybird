from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class GameOverScene(BaseMenuScene):
    def __init__(self, game):
        title = 'GameOver'
        options_list = ('Restart', 'Quit')

        super().__init__(game, title, *options_list)

    def perform_restart(self):
        from ..game.game_scene import GameScene

        self.game.set_scene(GameScene(game=self.game))

    def perform_quit(self):
        from .main_menu_scene import MainMenuScene

        self.game.set_scene(MainMenuScene(game=self.game))
