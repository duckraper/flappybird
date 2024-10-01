from typing import Union

import pygame as pg
from pygame.mixer import Sound

from src.core.game.settings import SFX_VOLUME
from src.resources.sounds import sfx


class AudioPlayer:
    @staticmethod
    def play_sound(sound: Union[str, 'Sound'], volume: float=1.0, loops: int=0, maxtime: int=0, fade_ms: int=0) -> None:
        if isinstance(sound, Sound):
            sound = sound
        elif isinstance(sound, str):
            sound_name = sound
            sound = sfx[sound_name]

        sound.set_volume(volume * SFX_VOLUME)
        sound.play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)

    @staticmethod
    def play_music(loops: int=0, start: float=0.0) -> None:
        pg.mixer.music.play(loops=loops, start=start)
