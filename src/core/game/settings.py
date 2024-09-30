from pathlib import Path

import pygame as pg

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # src/

FPS = 60

GAME_TITLE = 'FlappyBird'
GAME_ICON = pg.image.load(BASE_DIR.parent / 'assets' / 'img.ico')

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
    'chill': {
        'speed': SCREEN_WIDTH // 8,
        'spawn_rate': 2,
        'max_pipes_offset': SCREEN_HEIGHT // 1.5,
        'min_pipes_offset': SCREEN_HEIGHT // 3,
        'description': "This is the easiest difficulty, perfect for beginners. "
                       "The game will be slow and the pipes will be far apart."
    },
    'easy': {
        'speed': SCREEN_WIDTH // 4,
        'spawn_rate': 1.5,
        'max_pipes_offset': SCREEN_HEIGHT // 2,
        'min_pipes_offset': SCREEN_HEIGHT // 4,
        'description': "This is a beginner-friendly difficulty. "
                       "The game will be a bit faster and the pipes will be closer."
    },
    'medium': {
        'speed': SCREEN_WIDTH // 2.6,
        'spawn_rate': 1.3,
        'max_pipes_offset': SCREEN_HEIGHT // 4,
        'min_pipes_offset': SCREEN_HEIGHT // 5,
        'description': "This is the default difficulty. "
                       "The game will be fast and the pipes will be very close."
    },
    'hard': {
        'speed': SCREEN_WIDTH // 1.9,
        'spawn_rate': 1,
        'max_pipes_offset': SCREEN_HEIGHT // 5,
        'min_pipes_offset': SCREEN_HEIGHT // 6,
        'description': "This is a challenging difficulty. "
                       "The game will be very fast and the pipes will be extremely close."
    },
    'insane': {
        'speed': SCREEN_WIDTH // 1.5,
        'spawn_rate': 0.9,
        'max_pipes_offset': SCREEN_HEIGHT // 7,
        'min_pipes_offset': SCREEN_HEIGHT // 8,
        'description': "This is the hardest difficulty. "
                       "The game will be extremely fast and the pipes will be very close."
    },

}

