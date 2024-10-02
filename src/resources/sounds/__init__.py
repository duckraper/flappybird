import pygame as pg

from src.commons.assets_loader import AssetsLoader, ASSETS_DIR

pg.mixer.init()

SFX_DIR = ASSETS_DIR.joinpath('sounds').joinpath('sfx')
sfx_files = list(SFX_DIR.iterdir())

sfx = {
    f.stem:
        AssetsLoader.load_sound(SFX_DIR.joinpath(f), 0.08)
    for f in sfx_files
}
