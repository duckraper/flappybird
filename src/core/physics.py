class Physics:
    """Physics class to handle gravity and jumping for the bird"""
    def __init__(self, gravity: float=600, jump_force: float=250):
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
