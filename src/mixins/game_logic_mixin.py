class GameLogicMixin:
    def check_score(self):
        if self.pipes.sprites():
            pipe = self.pipes.sprites()[0]
            if not hasattr(pipe, 'scored') or not pipe.scored:
                if self.bird.sprite.rect.left > pipe.rect.right:
                    self.score += 1
                    pipe.scored = True
            # todo: hacer sonidito
