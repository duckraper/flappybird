from random import choice

from src.commons.audio_player import AudioPlayer
from src.commons.constants import FLAP_VOLUME, JUMP_FORCE, GRAVITY_FORCE
from src.core.game.settings import SCREEN_HEIGHT
from src.entities.abstracts import AnimatedSprite, CollidableSprite, BaseSprite, MovingSprite
from src.resources.spritesheets import bird_spritesheet


class Bird(AnimatedSprite,
           CollidableSprite,
           MovingSprite,
           BaseSprite):
    def __init__(self, x: int, y: int, jump_force: float = JUMP_FORCE):
        spritesheet = bird_spritesheet[choice(list(bird_spritesheet.keys()))]

        MovingSprite.__init__(self)
        AnimatedSprite.__init__(self, 16, *spritesheet)
        BaseSprite.__init__(self, x, y)

        self.rect: 'Rect' = self.image.get_rect(center=(self.x, self.y))

        self.jump_force = jump_force
        self.velocity_y = 0

    def jump(self, delta: float):
        self.set_current_frame(0)
        AudioPlayer.play_sound('flap', volume=FLAP_VOLUME)

        if not self.get_animating():
            self.set_animating(True)

        self.set_speed(vy=-self.jump_force)

    def constraints(self):
        if self.rect.top < 0:
            self.y = 0 + self.image.get_height() // 2
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.image.get_height() // 2
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, delta: float):
        self.animate(delta)
        self.move(delta)
        self.rect.center = (self.x, self.y)

        super().update(delta)