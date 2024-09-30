from pathlib import Path
from typing import Union

import pygame as pg

from src.core.game.settings import BASE_DIR

ASSETS_DIR = BASE_DIR.parent.joinpath('assets')  # src/assets
SPRITES_DIR = ASSETS_DIR.joinpath('images', 'sprites')


class AssetsLoader:
    @staticmethod
    def load_image(filepath: Path | str) -> 'Surface':
        if not pg.display.get_init():
            pg.display.set_mode((1, 1))
        return pg.image.load(filepath).convert_alpha()

    @staticmethod
    def load_sprites(directory: Path | str,
                     file_pattern: str,
                     size: tuple[int, int],
                     colorkey=None) -> Union[list['Surface'], 'Surface']:
        """
         usage:
            sprite = load_sprites("path/to/spritesheet", "sprite_name-0{i}.png", (50, 50), (0, 0, 0))
            where n is the number of the sprite frame
        """
        imgs_dir: Path = SPRITES_DIR.joinpath(directory)

        sprite_list: list[pg.surface.Surface] = []
        files_amount: int = len(list(imgs_dir.iterdir()))
        for i in range(files_amount):
            sprite_path: Path = imgs_dir.joinpath(file_pattern.format(i=i))
            frame: pg.surface.Surface = pg.transform.scale(AssetsLoader.load_image(str(sprite_path)), size)

            if colorkey is not None:
                frame.set_colorkey(colorkey)

            sprite_list.append(frame)

        return sprite_list \
            if len(sprite_list) > 1 \
            else sprite_list[0]

    @staticmethod
    def load_music(filepath: Path | str) -> None:
        if not pg.mixer.get_init():
            pg.mixer.init()
        pg.mixer.music.load(filepath)

    @staticmethod
    def load_sound(filepath: Path | str, volume: float=1.0) -> 'Sound':
        if not pg.mixer.get_init():
            pg.mixer.init()
        sound = pg.mixer.Sound(filepath)
        sound.set_volume(volume)
        return sound
