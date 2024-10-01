from src.commons.constants import FLOOR_WIDTH, SCREEN_WIDTH
from src.commons.constants import FLOOR_Y
from src.entities.sprites.floor import Floor


class FloorSpawnerMixin:
    last_spawned_right_x = 0

    def spawn_floor(self) -> None:
        max_floor_sprites_in_screen = SCREEN_WIDTH // FLOOR_WIDTH + 2

        while len(self.manager.floor.sprites()) < max_floor_sprites_in_screen:
            new_floor = self.create_floor()

            self.manager.floor.add(new_floor)
            self.manager.sprites.add(new_floor)

    def create_floor(self) -> Floor:
        floor_sprites = self.manager.floor.sprites()
        x = 0

        if len(floor_sprites) > 0:
            velocity = floor_sprites[0].vx * self.manager.scene.game.get_delta()
            x = floor_sprites[-1].rect.right - velocity

        return Floor(x, FLOOR_Y, speed=self.manager.game_speed)
