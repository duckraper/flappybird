import functools
from typing import Union

from src.commons.audio_player import AudioPlayer


def has_sfx(sfx: Union[str, 'Sound', 'SoundType'], volume: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            AudioPlayer.play_sound(sfx, volume)
            return func(*args, **kwargs)

        return wrapper

    return decorator
