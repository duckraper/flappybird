import pygame as pg


class GameEvent:
    CONFIG_CHANGE = pg.USEREVENT + 1

    @staticmethod
    def create_config_change_event(config_name, new_value):
        return pg.event.Event(GameEvent.CONFIG_CHANGE, {
            'config_name': config_name, 'new_value': new_value
        })
