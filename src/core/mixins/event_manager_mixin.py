import pygame as pg


class EventManagerMixin:
    def process_events_but_input(self):
        for event in pg.event.get(exclude=(pg.KEYDOWN, pg.KEYUP)):
            if event.type == pg.QUIT:
                self.stop_running()
                break
        pass

    def handle_events(self, event):
        pass
