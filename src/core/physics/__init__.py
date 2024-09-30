from src.commons.constants import GRAVITY_FORCE, JUMP_FORCE


class Physics:
    def __init__(self, gravity: float = GRAVITY_FORCE, jump_force: float = JUMP_FORCE):
        self.gravity = gravity
        self.jump_force = jump_force
        self.velocity = 0

    def apply_gravity(self, delta: float):
        self.velocity += self.gravity * delta

    def jump(self):
        self.velocity = -self.jump_force

    def update_position(self, y: int, delta: float) -> float:
        self.apply_gravity(delta)
        return y + self.velocity * delta
