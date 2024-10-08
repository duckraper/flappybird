from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class HighScoresScene(BaseMenuScene):
    # TODO: terminar esta escena, y gestionar como hacerla funcionar
    def __init__(self, game):
        options_list = [
            'Return',
        ]
        super().__init__(game, 'HighScores', *options_list)

    def perform_return(self):
        from .main_menu_scene import MainMenuScene

        self.stop_running()
        self.change_scene(MainMenuScene(game=self.game))
