from src.scenes import BaseScene


class SceneManagerMixin:
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
