from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class HighScoresScene(BaseMenuScene):
    # TODO: terminar esta escena, y gestionar como hacerla funcionar
    def __init__(self, game, **kwargs):
        options_list = [
            'Return',
        ]
        super().__init__(game, 'HighScores', *options_list, **kwargs)

    def perform_return(self):
        self.stop_running()
        menu = self.game.scenes_stack.pop()
        self.change_scene(menu)

