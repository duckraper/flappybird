from time import time

class SpriteManagerMixin:
    def spawn_pipes(self):
        now = time()
        if now - self.last_spawn_time > self.spawn_rate:
            self.last_spawn_time = now
            pipes = self.spawner('pipe')
            self.pipes.add(pipes)

            self.sprites.add(pipes)

    def update_all_sprites(self):
        self.spawn_pipes()

        self.sprites.update(delta=self.scene.game.delta)

    def draw_all_sprites(self):
        self.sprites.draw(self.screen)

        self.floor.draw(self.screen)
