import pygame as pg
from pygame._sprite import collide_mask


class GameLogicMixin:
    def check_score(self):
        if self.pipes.sprites():
            pipe = self.pipes.sprites()[0]
            if not hasattr(pipe, 'scored') or not pipe.scored:
                if self.bird.sprite.rect.left > pipe.rect.right:
                    self.score += 1
                    pipe.scored = True
            # todo: hacer sonidito

    def handle_collisions(self):
        if self.collided(self.bird.sprite, self.floor):
            # self.perform_game_over()
            print('collided')

        if self.collided(self.bird.sprite, self.pipes):
            # self.perform_game_over()
            print('collided')