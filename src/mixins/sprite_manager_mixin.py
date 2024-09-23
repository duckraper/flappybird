from pygame.sprite import Group

from src.services.spawners.mixins.pipe_spawner_mixin import PipeSpawnerMixin

class SpriteManagerMixin:

    def update_all_sprites(self):
        # self.sprites.add(self.pipes)

        self.sprites.update(delta=self.scene.game.delta)

    def draw_all_sprites(self):
        self.sprites.draw(self.screen)
