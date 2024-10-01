from src.commons.abstracts import BaseTextRenderer
from src.core.game.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class ScoreRenderer(BaseTextRenderer):
    def __init__(self, scene):
        super().__init__()
        self.scene: 'GameScene' = scene

    def __call__(self):
        self.render()

    def render(self):
        screen = self.scene.game.get_screen()

        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 12

        super().render(surface=screen,
                       position=(x, y),
                       text=str(self.scene.manager.score),
                       font_size=SCREEN_WIDTH // 11,
                       outline_width=2,
                       shadow_width=2)
