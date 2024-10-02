from src.commons.constants import BG_SPEED, DEFAULT_BG_ALPHA, DEFAULT_BG_LAYER
from src.entities.abstracts import CommonSprite, SolidSprite, MovingSprite


class Background(SolidSprite,
                 MovingSprite,
                 CommonSprite):
    def __init__(self, image: 'Surface', x = 0, y = 0, **kwargs):
        vx = kwargs.get('vx', BG_SPEED)
        self.alpha = kwargs.get('alpha', DEFAULT_BG_ALPHA)
        self.image.set_alpha(self.alpha)
        self.layer = kwargs.get('layer', DEFAULT_BG_LAYER)

        MovingSprite.__init__(self, vx=vx)
        CommonSprite.__init__(self, image, x, y, hasnt_mask=True, topleft=(x, y))

    def constraints(self) -> None:
        if self.rect.left < 0 and not hasattr(self, 'next_bg'):
            self.next_bg = self.__class__(self.image.copy(),
                                          x=self.rect.right,
                                          alpha=self.alpha)
            group = self.groups()[0]
            if hasattr(group, 'layer'):
                group.add(self.next_bg, layer=self.layer)
                return
            group.add(self.next_bg)

    def update(self, delta: float) -> None:
        self.move_x(delta)
        self.constraints()
