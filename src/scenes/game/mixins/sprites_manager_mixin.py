from pygame.sprite import Group

class SpriteManagerMixin:
    def update_all_sprites(self):
        sprites: Group = self.sprites
        sprites.update(delta=self.game.delta)

    def draw_all_sprites(self):
        sprites: Group = self.sprites
        sprites.draw(self.game.screen)
