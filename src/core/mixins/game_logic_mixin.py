import time


class GameLogicMixin:
    waiting_time = 1

    def check_score(self):
        if self.pipes.sprites():
            pipe = self.pipes.sprites()[0]
            if not hasattr(pipe, 'scored') or not pipe.scored:
                if self.bird.sprite.rect.left > pipe.rect.right:
                    self.score += 1
                    pipe.scored = True
            # todo: hacer sonidito

    def handle_collisions(self):
        bird = self.bird.sprite

        if self.collided(bird, self.floor):
            # todo: dar tiempo de espera luego de la colision para el geimover
            # TODO: tengo suenio, seguirlo todo alberro eqis

            self.perform_game_over()

        if self.collided(bird, self.pipes):
            for sprite in self.sprites.sprites():
                if hasattr(sprite, 'speed'):
                    sprite.set_moving(False)
                    self.game_over = True
