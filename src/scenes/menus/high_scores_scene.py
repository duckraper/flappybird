from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene
from pprint import pprint

class HighScoresScene(BaseMenuScene):
    # TODO: terminar esta escena, y gestionar como hacerla funcionar
    def __init__(self, game, **kwargs):
        options_list = [
            'Return',
        ]
        super().__init__(game, 'HighScores', *options_list, **kwargs)
    def startup(self):
        super().startup()
        pprint(f'HighScores:'
              f'{self.game.score_manager.get_top_scores()}')
#! todo: se acaba la generacion del fondo de la escena: fix
    def perform_return(self):
        self.stop_running()
        menu = self.game.scenes_stack.pop()
        self.change_scene(menu)

