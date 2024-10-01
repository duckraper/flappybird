from src.commons.audio_player import AudioPlayer
from src.commons.constants import SCORE_VOLUME, HIT_VOLUME
from src.entities.abstracts import MovingSprite


class GameLogicMixin:
    waiting_time = 1

    def check_score(self):
        if self.pipes.sprites():
            pipe = self.pipes.sprites()[0]
            if not hasattr(pipe, 'scored') or not pipe.scored:
                if self.bird.sprite.rect.left > pipe.rect.right:
                    AudioPlayer.play_sound('score', SCORE_VOLUME)
                    self.score += 1
                    pipe.scored = True

    def handle_collisions(self):
        bird = self.bird.sprite

        if self.collided(bird, self.floor):
            self.perform_game_over()

        if self.collided(bird, self.pipes):
            AudioPlayer.play_sound('hit', volume=HIT_VOLUME)
            for sprite in self.sprites.sprites():
                if isinstance(sprite, MovingSprite):
                    sprite.set_moving(False)
                    # todo: arreglar el sonido de los tubos
            self.game_over = True
