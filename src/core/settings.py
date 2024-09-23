import pygame as pg

FPS = 60

GAME_TITLE = 'FlappyBird'

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_SIZE: tuple[int, int] = (SCREEN_WIDTH, SCREEN_HEIGHT)

GRAVITY_FORCE = 1000
JUMP_FORCE = 380

FLOOR_HEIGHT = SCREEN_HEIGHT // 10
FLOOR_Y = SCREEN_HEIGHT - FLOOR_HEIGHT

INGAME_DEADZONE = (SCREEN_HEIGHT // 5,
                   FLOOR_Y - SCREEN_HEIGHT // 5)

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
    'easy': {
        'speed': 200,
        'spawn_rate': 1.5,
        'max_pipes_offset': SCREEN_HEIGHT // 2,
        'min_pipes_offset': SCREEN_HEIGHT // 4
    },
    'medium': {
        'speed': 300,
        'spawn_rate': 1.3,
        'max_pipes_offset': SCREEN_HEIGHT // 4,
        'min_pipes_offset': SCREEN_HEIGHT // 5
    },
    'hard': {
        'speed': 420,
        'spawn_rate': 1,
        'max_pipes_offset': SCREEN_HEIGHT // 5,
        'min_pipes_offset': SCREEN_HEIGHT // 6
    },
    'insane': {
        'speed': 560,
        'spawn_rate': 0.9,
        'max_pipes_offset': SCREEN_HEIGHT // 7,
        'min_pipes_offset': SCREEN_HEIGHT // 8
    }
}
