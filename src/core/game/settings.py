import configparser as cp
from pathlib import Path

import pygame as pg

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # src/
DATA_DIR = BASE_DIR.parent / 'data'

config = cp.ConfigParser()
config.read(DATA_DIR / 'config.ini')

# screne confg
FPS = 120
GAME_TITLE = 'FlappyBird'
GAME_ICON = pg.image.load(BASE_DIR.parent / 'assets' / 'img.ico')

SCREEN_SIZE = tuple(int(i) for i in config.get('Display', 'resolution').split('x'))
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE

MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.8

SCORE_VOLUME = 0.8 * SFX_VOLUME
DIE_VOLUME = 0.8 * SFX_VOLUME
HIT_VOLUME = 0.8 * SFX_VOLUME
SWOOSH_VOLUME = 0.4 * SFX_VOLUME
FLAP_VOLUME = 0.4 * SFX_VOLUME

# difificulty
DIFFICULTY = config.get('Game', 'difficulty')
DIFFICULTY_LEVELS = {
    'chill': {
        'speed': SCREEN_WIDTH // 8,
        'spawn_rate': 5,
        'max_pipes_y_offset': SCREEN_HEIGHT // 1.5,
        'min_pipes_y_offset': SCREEN_HEIGHT // 3,
        'pipes_x_offset': SCREEN_WIDTH // 2,
        'description': "This is the easiest difficulty, perfect for beginners. "
                       "The game will be slow and the pipes will be far far apart."
    },
    'easy': {
        'speed': SCREEN_WIDTH // 4,
        'spawn_rate': 1.7,
        'max_pipes_y_offset': SCREEN_HEIGHT // 2,
        'min_pipes_y_offset': SCREEN_HEIGHT // 4,
        'pipes_x_offset': SCREEN_WIDTH // 2.6,
        'description': "This is a beginner-friendly difficulty. "
                       "The game will be a bit faster and the pipes will be closer."
    },
    'medium': {
        'speed': SCREEN_WIDTH // 2.6,
        'spawn_rate': 1.2,
        'max_pipes_y_offset': SCREEN_HEIGHT // 4,
        'min_pipes_y_offset': SCREEN_HEIGHT // 5,
        'pipes_x_offset': SCREEN_WIDTH // 3.2,
        'description': "This is the default difficulty. "
                       "The game will be fast and the pipes will be very close."
    },
    'hard': {
        'speed': SCREEN_WIDTH // 1.8,
        'spawn_rate': 0.9,
        'max_pipes_y_offset': SCREEN_HEIGHT // 6,
        'min_pipes_y_offset': SCREEN_HEIGHT // 7,
        'pipes_x_offset': SCREEN_WIDTH // 2.1,
        'description': "This is a challenging difficulty. "
                       "The game will be very fast and the pipes will be extremely close."
    },
    'insane': {
        'speed': SCREEN_WIDTH // 1.5,
        'spawn_rate': 0.9,
        'max_pipes_y_offset': SCREEN_HEIGHT // 7,
        'min_pipes_y_offset': SCREEN_HEIGHT // 8,
        'pipes_x_offset': SCREEN_WIDTH // 2.4,
        'description': "This is the hardest difficulty. "
                       "The game will be extremely fast and the pipes will be very close."
    },
}

# bindings (unmutable)
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
