from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class GameOverScene(BaseMenuScene):
    def __init__(self, game, score, **kwargs):
        title = 'GameOver'
        options_list = ('Restart', 'Quit')

        self.highest_score = score > game.score_manager.get_highest_score()
        self.did_nothing = score == 0

        captions = [f'Score: {score}']

        if self.highest_score:
            captions.append('New High Score!!!')
        elif self.did_nothing:
            captions.append('Dude... You need to play!')
        else:
            captions.append('Play Again?!')

        super().__init__(game, title, [*captions], *options_list, **kwargs)

    def draw(self, *args, **kwargs):
        if self.highest_score:
            font_color = (255, 215, 0)
        elif self.did_nothing:
            font_color = (200, 20, 20)
        else:
            font_color = (244, 213, 141)

        super().draw(caption_font_color=font_color,
                     caption_font_size=60,
                     caption_options_offset=50,
                     title_margin=85)

    def perform_restart(self):
        from ..game.game_scene import GameScene

        self.change_scene(GameScene(game=self.game))

    def perform_quit(self):
        menu = self.game.scenes_stack.pop()

        self.change_scene(menu)
