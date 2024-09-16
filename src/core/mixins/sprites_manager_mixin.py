import pygame as pg

class SpriteManagerMixin:
    def update_all_sprites(self):
        sprites = self.get_all_sprites()
        sprites.update()

    def draw_all_sprites(self):
        sprites = self.get_all_sprites()
        sprites.draw(self.get_screen())

