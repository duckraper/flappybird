from src.core.game.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from src.entities.sprites import Bird


class BirdSpawnerMixin:
    def spawn_bird(self):
        x, y = self.__get_bird_starting_coords()
        return Bird(x, y)

    @staticmethod
    def __get_bird_starting_coords():
        x = SCREEN_WIDTH // 6
        y = SCREEN_HEIGHT // 2

        return x, y
