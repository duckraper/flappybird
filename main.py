import sys
import pygame as pg
from src.core.game import Game

def main():
    pg.init()

    game = Game(title='Flappy Bird')
    game.run()

    sys.exit(0)


if __name__ == '__main__':
    main()
