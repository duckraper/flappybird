from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class PauseMenuScene(BaseMenuScene):
    def __init__(self, game):
        options_list = [
            'Resume',
            'Restart',
            'Main Menu'
        ]
        super().__init__(game, 'Paused Game', *options_list, )

    def perform_resume(self):
        scene = self.game.scenes_stack.pop()

        self.stop_running()
        self.game.set_scene(scene)

        scene.running = True

    def perform_restart(self):
        scene = self.game.scenes_stack.pop()

        self.stop_running()
        self.game.set_scene(scene.__class__(game=self.game))

    def perform_main_menu(self):
        from .main_menu_scene import MainMenuScene

        scene = self.game.scenes_stack.pop()

        self.stop_running()
        self.game.set_scene(MainMenuScene(game=self.game))
