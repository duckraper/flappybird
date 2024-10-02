from abc import ABC, abstractmethod


class ISprite(ABC):
    @abstractmethod
    def constraints(self) -> None:
        pass

    @abstractmethod
    def update(self, delta) -> None:
        pass

    @abstractmethod
    def get_position(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def set_position(self, x: int, y: int) -> None:
        pass


class IMovingSprite(ABC):
    @abstractmethod
    def get_speed(self) -> float:
        pass

    @abstractmethod
    def set_speed(self, speed: float) -> None:
        pass

    @abstractmethod
    def get_moving(self) -> bool:
        pass

    @abstractmethod
    def set_moving(self, moving: bool) -> None:
        pass

    @abstractmethod
    def move(self, delta: float) -> None:
        pass


class IAnimatedSprite(ABC):
    @abstractmethod
    def get_current_frame(self) -> int:
        pass

    @abstractmethod
    def set_current_frame(self, frame: int) -> None:
        pass

    @abstractmethod
    def get_animating(self) -> bool:
        pass

    @abstractmethod
    def set_animating(self, animating: bool) -> None:
        pass


class ICollidableSprite(ABC):
    @abstractmethod
    def check_collision(self, other: 'ISprite', collide_mask: bool) -> bool:
        pass

    @abstractmethod
    def on_collision(self, other: 'ISprite') -> None:
        pass

    @abstractmethod
    def resolve_collision(self, other: 'ISprite') -> None:
        pass


class ISolidSprite(ABC):
    pass
