import sys

import pygame as pg


def main() -> None:
    pg.init()
    pg.display.init()
    pg.display.set_mode((1, 1))
    pg.mixer.init()
    pg.font.init()

    from src.core.game import Game, settings as s

    game = Game(
        title=s.GAME_TITLE,
        icon=s.GAME_ICON
    )

    game.run()
    sys.exit(0)

if __name__ == '__main__':
    main()
