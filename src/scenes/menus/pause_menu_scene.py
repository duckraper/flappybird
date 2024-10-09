from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class PauseMenuScene(BaseMenuScene):
    def __init__(self, game, **kwargs):
        options_list = [
            'Resume',
            'Restart',
            'Main Menu'
        ]
        super().__init__(game, 'Paused Game', *options_list, **kwargs)

    def perform_resume(self):
        self.stop_running()

        game_scene = self.game.scenes_stack.pop(start_current=False)

        self.change_scene(game_scene)


    def perform_restart(self):
        scene = self.game.scenes_stack.pop()

        self.stop_running()
        self.change_scene(scene.__class__(game=self.game))

    def perform_main_menu(self):
        self.stop_running()

        self.game.scenes_stack.pop()

        menu = self.game.scenes_stack.pop()
        self.change_scene(menu)
