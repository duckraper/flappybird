from datetime import datetime

from src.core.game.settings import SCREEN_HEIGHT
from src.scenes.menus.abstracts.base_menu_scene import BaseMenuScene


class HighScoresScene(BaseMenuScene):
    def __init__(self, game, **kwargs):
        options_list = [
            'Return',
        ]
        top_scores = game.score_manager.get_top_scores(ls=5)

        scores_list = [
            f' {i + 1} I {datetime.strptime(score["date"], "%Y-%m-%d %H:%M:%S.%f").strftime("%d-%m-%Y %H:%M:%S")} I {str(score["score"]).rjust(3)}'
            for i, score in enumerate(top_scores)
        ]

        empty_slots = 5 - len(top_scores)
        scores_list.extend(
            [f' {i + len(top_scores) + 1} I --------- -------- I ---' for i in range(empty_slots)]
        )
        header = '  o        Date         Score'
        table = [header] + scores_list
        super().__init__(game, 'HighScores', [*table], *options_list, **kwargs)

    def startup(self):
        super().startup()

    def draw(self, *args, **kwargs):
        super().draw(title_margin=50,
                     caption_font_color=(244, 213, 141),
                     caption_font_size=55,
                     caption_options_offset=50,
                     y_forzada=SCREEN_HEIGHT // 1.15)

    def update(self, *args, **kwargs):
        super().update()

    def perform_return(self):
        self.stop_running()
        menu = self.game.scenes_stack.pop()
        self.change_scene(menu)
