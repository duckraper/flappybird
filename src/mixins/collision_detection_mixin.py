import pygame as pg


class CollisionDetectionMixin:
    def check_collisions(self):
        self.check_collision_with_floor(self.bird.sprite, [self.floor.sprite])
        self.check_collision_with_pipes(self.bird.sprite, self.pipes)

    def check_collision_with_floor(self, sprite, group):
        if pg.sprite.spritecollide(sprite, group, False):
            print('collision with floor, do smthng')

    def check_collision_with_pipes(self, sprite, group):
        if pg.sprite.spritecollide(sprite, group, False):
            print('collision with pipes, do smthng')
