import pygame as pg

FPS = 60

GAME_TITLE = 'FlappyBird'

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_SIZE: tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)

MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.7

KEY_BINDINGS = {
    'esc': pg.K_ESCAPE,
    'space': pg.K_SPACE,
    'p': pg.K_p,
    'w': pg.K_w,
    'q': pg.K_q,
    'up': pg.K_UP,
    'down': pg.K_DOWN,
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'enter': pg.K_RETURN
}

DIFFICULTY_LEVELS = {
    'easy': {'speed': 5, 'spawn_rate': 4},
    'medium': {'speed': 7, 'spawn_rate': 3},
    'hard': {'speed': 10, 'spawn_rate': 1},
    'insane': {'speed': 15, 'spawn_rate': 1}
}
