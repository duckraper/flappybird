import pygame as pg

FPS = 60

GAME_TITLE = 'Flappy Bird'

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_SIZE: tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)

MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.7

KEY_BINDINGS = {
    'jump': pg.K_SPACE,
    'pause': pg.K_p,
    'up': pg.K_UP,
    'down': pg.K_DOWN,
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'enter': pg.K_RETURN
}

DIFFICULTY_LEVELS = {
    'easy': {'speed': 5, 'spawn_rate': 3},
    'medium': {'speed': 7, 'spawn_rate': 2},
    'hard': {'speed': 10, 'spawn_rate': 1},
    'insane': {'speed': 15, 'spawn_rate': 1}
}
