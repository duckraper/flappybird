from random import choice

from src.commons.constants import BG_SPEED, DEFAULT_BG_ALPHA, DEFAULT_BG_LAYER
from src.core.game.settings import SCREEN_WIDTH
from src.entities.sprites.abstracts import CommonSprite, SolidSprite, MovingSprite
from src.resources.backgrounds import backgrounds


class Background(SolidSprite,
                 MovingSprite,
                 CommonSprite):
    def __init__(self, image: 'Surface'=None, x=0, y=0, **kwargs):
        if image is None:
            image = choice(backgrounds).copy()
        vx = kwargs.get('vx', BG_SPEED)

        MovingSprite.__init__(self, vx=vx)
        CommonSprite.__init__(self, image, x, y, hasnt_mask=True, topleft=(x, y))

        self.alpha = kwargs.get('alpha', DEFAULT_BG_ALPHA)
        self.image.set_alpha(self.alpha)
        self.layer = kwargs.get('layer', DEFAULT_BG_LAYER)

    def constraints(self) -> None:
        if self.vx < 0:
            if (self.rect.left < 0 or self.rect.right < SCREEN_WIDTH) and not hasattr(self, 'next_bg'):
                self.next_bg = self.__class__(self.image.copy(),
                                              x=self.rect.right-0.5,
                                              alpha=self.alpha,
                                              vx=self.vx)
                group = self.groups()[0]
                if hasattr(group, 'layer'):
                    group.add(self.next_bg, layer=self.layer)
                    return
                group.add(self.next_bg)

    def update(self, delta: float) -> None:
        self.move_x(delta)
        self.constraints()
