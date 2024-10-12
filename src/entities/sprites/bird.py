from random import choice

from src.commons.audio_player import AudioPlayer
from src.commons.constants import JUMP_FORCE
from src.commons.helpers import is_between
from src.core.game.settings import SCREEN_HEIGHT, FLAP_VOLUME
from src.entities.sprites.abstracts import AnimatedSprite, CollidableSprite, BaseSprite, MovingSprite
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

    def on_collision(self, other: 'CollidableSprite') -> None:
        from src.entities.sprites.pipe import Pipe
        from src.entities.sprites.floor import Floor

        if isinstance(other, Pipe):
            # hits on the left
            if is_between(other.rect.left, self.rect.left, self.rect.right):
                self.rect.right = other.rect.left
                self.set_speed(vx=other.vx)
            # hits on the right
            elif is_between(other.rect.right, self.rect.left, self.rect.right):
                self.rect.left = other.rect.right
                self.set_speed(vx=-other.vx)

        elif isinstance(other, Floor):
            self.rect.bottom = other.rect.top

    def jump(self, delta: float):
        self.set_current_frame(0)
        AudioPlayer.play_sound('flap', volume=FLAP_VOLUME)

        if not self.get_animating():
            self.set_animating(True)

        self.set_speed(vy=-self.jump_force)

    def constraints(self):
        if self.rect.top < 0:
            self.rect.top = 0
            self.y = self.rect.height // 2

        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y = SCREEN_HEIGHT - self.rect.height // 2

    def update(self, delta: float):
        self.animate(delta)
        self.move(delta)
        self.rect.center = (self.x, self.y)

        self.constraints()
