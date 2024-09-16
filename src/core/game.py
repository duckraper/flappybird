import pygame as pg
from src.core.mixins import EventManagerMixin, SpriteManagerMixin
from src.core.generics import BaseGame
from src.core.settings import FPS, BASE_COLOR
from src.utils import Debug

class Game(EventManagerMixin,
           SpriteManagerMixin,
           BaseGame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'title' in kwargs:
            title = kwargs['title']
            pg.display.set_caption(title)

        self.debugger = Debug()
        self.sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        self.bird = pg.sprite.GroupSingle()

    def get_all_sprites(self):
        return self.sprites

    def perform_rendering(self):
        self.screen.fill(BASE_COLOR)
        self.draw_all_sprites()
        self.debugger.draw(info=self.clock.get_fps())

        pg.display.flip()

    def update(self):
        self.process_events()
        self.update_all_sprites()
        self.perform_rendering()

        self.clock.tick(FPS)

    def run(self):
        while self.running:
            self.update()
        pg.quit()
