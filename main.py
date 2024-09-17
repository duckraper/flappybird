import sys
import pygame as pg
from src.core.game import Game

def main():
    pg.init()
    pg.font.init()

    game = Game()
    game.run()

    sys.exit(0)


if __name__ == '__main__':
    main()
