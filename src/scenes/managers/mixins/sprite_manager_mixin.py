class SpriteManagerMixin:
    def update_all_sprites(self):
        self.sprites.update(delta=self.scene.game.delta)

    def draw_all_sprites(self):
        self.sprites.draw(self.screen)

        self.floor.draw(self.screen)

    def spawn_sprites(self):
        if not self.game_over:
            self.spawner('floor')
            self.spawner('pipe')
