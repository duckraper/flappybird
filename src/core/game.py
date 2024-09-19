import pygame as pg
from src.core.mixins import EventManagerMixin, SpriteManagerMixin
from src.core.generics import BaseGame
from src.core.settings import FPS
from src.utils import Debug, BASE_COLOR
from src.scenes import MainMenuScene


class Game(EventManagerMixin,
           SpriteManagerMixin,
           BaseGame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.debugger = Debug()
        self.sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        self.bird = pg.sprite.GroupSingle()
        self.scene = MainMenuScene(game=self)

        self.high_score = 0

    def startup(self):
        super().startup()

    def get_all_sprites(self):
        return self.sprites

    def perform_rendering(self):
        self.screen.fill(BASE_COLOR)
        self.scene.draw()
        self.draw_all_sprites()
        self.debugger.draw(info=self.scene.selected_option_name)
        # TODO terminar de implementar el menu

        pg.display.flip()

    def update(self):
        self.process_events_but_input()
        self.update_all_sprites()
        self.scene.update()

    def run(self):
        while self.running:
            self.update()
            self.perform_rendering()

            self.clock.tick(FPS)
        pg.quit()
