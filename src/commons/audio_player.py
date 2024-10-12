from random import randint
from typing import Union, Optional

import pygame as pg
from pygame.mixer import Sound

from src.core.game.settings import SFX_VOLUME, MUSIC_VOLUME
from src.resources.music import music
from src.resources.sounds import sfx


class AudioPlayer:
    @staticmethod
    def play_sound(sound: Union[str, 'Sound'], volume: float = 1.0, loops: int = 0, maxtime: int = 0,
                   fade_ms: int = 0) -> None:
        if isinstance(sound, Sound):
            sound = sound
        elif isinstance(sound, str):
            sound_name = sound
            sound = sfx[sound_name]

        sound.set_volume(volume * SFX_VOLUME)
        sound.play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)

    @staticmethod
    def set_music(filepath: Optional[Union[str, 'Path']] = None, volume: float = MUSIC_VOLUME) -> None:
        if not filepath:
            filepath = music[f'track-0{randint(0, len(music.keys()) - 1)}']
        if not pg.mixer.get_init():
            pg.mixer.init()
        if pg.mixer.music.get_busy():
            AudioPlayer.stop_music()
        pg.mixer.music.load(filepath)
        pg.mixer.music.set_volume(volume)

    @staticmethod
    def play_music(loops: int = 0, start: float = 0.0) -> None:
        pg.mixer.music.play(loops=loops, start=start)

    @staticmethod
    def is_playing_music() -> bool:
        print(pg.mixer.music.get_busy())
        return pg.mixer.music.get_busy()

    @staticmethod
    def pause_music():
        pg.mixer.music.pause()

    @staticmethod
    def resume_music():
        pg.mixer.music.unpause()

    @staticmethod
    def stop_music():
        pg.mixer.music.stop()
