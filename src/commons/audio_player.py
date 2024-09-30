import pygame as pg


class AudioPlayer:
    @staticmethod
    def play_sound(sound: 'Sound', loops: int=0, maxtime: int=0, fade_ms: int=0) -> None:
        sound.play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)

    @staticmethod
    def play_music(loops: int=0, start: float=0.0) -> None:
        pg.mixer.music.play(loops=loops, start=start)
