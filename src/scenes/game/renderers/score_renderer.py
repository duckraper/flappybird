from src.commons.abstracts import BaseTextRenderer
from src.core.game.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class ScoreRenderer(BaseTextRenderer):
    # todo: integrar con score_manager
    def __init__(self, scene):
        super().__init__()
        self.scene: 'GameScene' = scene
        self.highest_score = self.scene.game.score_manager.get_highest_score()

    def __call__(self):
        self.render()

    def render(self):
        screen = self.scene.game.get_screen()

        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 12

        color = 'white' \
            if self.scene.manager.score < self.highest_score \
            else 'gold'

        super().render(surface=screen,
                       position=(x, y),
                       font_color=color,
                       text=str(self.scene.manager.score),
                       font_size=SCREEN_HEIGHT // 8,
                       outline_width=2,
                       shadow_width=2)
