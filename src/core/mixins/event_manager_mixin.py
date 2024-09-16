import pygame as pg

class EventManagerMixin:
    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.stop_running()
                break
