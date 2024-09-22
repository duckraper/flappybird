from src.scenes.base.base_menu_scene import BaseMenuScene


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
        self.game.set_scene(MainMenuScene(game=self.game))
