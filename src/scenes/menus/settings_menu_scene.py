from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class SettingsScene(BaseMenuScene):
    def __init__(self, game):
        options_list = [
            'Return',
        ]
        super().__init__(game, 'Settings', *options_list)

    def perform_return(self):
        from .main_menu_scene import MainMenuScene

        self.stop_running()
        self.game.set_scene(MainMenuScene(game=self.game))
