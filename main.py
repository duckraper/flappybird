import sys

import pygame as pg

from src.core.game import Game
from src.core.game.settings import GAME_ICON, GAME_TITLE


def main():
    pg.init()

    game = Game(
        title=GAME_TITLE,
        icon=GAME_ICON
    )
    game.run()

    sys.exit(0)


if __name__ == '__main__':
    main()
