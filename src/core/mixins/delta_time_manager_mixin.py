from time import time


class DeltaTimeManagerMixin:
    elapsed_time: float = time()
    delta: float = time() - elapsed_time

    def update_delta(self):
        self.delta = time() - self.elapsed_time
        self.elapsed_time = time()

    def get_delta(self) -> float:
        return self.delta