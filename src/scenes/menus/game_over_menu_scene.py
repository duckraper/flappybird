from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class GameOverScene(BaseMenuScene):
    # TODO: mejorar para que muestre
    #       en la escena el score, y si rompi el highest score
    def __init__(self, game, **kwargs):
        title = 'GameOver'
        options_list = ('Restart', 'Quit')

        super().__init__(game, title, ['asdasd'], *options_list, **kwargs)

    def perform_restart(self):
        from ..game.game_scene import GameScene

        self.change_scene(GameScene(game=self.game))

    def perform_quit(self):
        menu = self.game.scenes_stack.pop()

        self.change_scene(menu)
