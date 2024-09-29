from src.scenes.abstracts.base_scene import BaseScene
from src.scenes.utils.scenes_stack import ScenesStack


class SceneManagerMixin:
    scenes_stack = ScenesStack()

    def set_scene(self, scene: BaseScene):
        if scene is None:
            self.scene.stop_running()

        self.scene = scene

    def draw_scene(self, *args, **kwargs):
        if self.scene:
            self.scene.draw(*args, **kwargs)

    def update_scene(self, *args, **kwargs):
        if self.scene:
            self.scene.update(*args, **kwargs)
