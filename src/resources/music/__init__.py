import pygame as pg

from src.commons.assets_loader import ASSETS_DIR

pg.mixer.init()

MUSIC_DIR = ASSETS_DIR.joinpath('sounds').joinpath('music')
music_files = list(MUSIC_DIR.iterdir())

music = {
    # track-0i.mp3
    f.stem: f
    for f in music_files
}
