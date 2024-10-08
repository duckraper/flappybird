import pygame as pg

from src.core.events import GameEvent


class EventManagerMixin:
    def process_events_but_input(self):
        for event in pg.event.get(exclude=(pg.KEYDOWN, pg.KEYUP, pg.MOUSEMOTION)):
            self.handle_events(event)

    def handle_events(self, event):
        if event.type == GameEvent.CONFIG_CHANGE:
            self.export_config()
        if event.type == pg.QUIT:
            self.stop_running()
