from enum import IntEnum

from src.commons.decorators import has_sfx
from src.core.game.settings import SWOOSH_VOLUME
from src.scenes.managers.mixins import MenuRendererMixin


class MenuActionsManger(MenuRendererMixin):
    def __init__(self, menu: 'BaseMenuScene', *options):
        self.menu = menu
        self.menu_title = menu.title
        self.captions = menu.captions

        self.menu_option = IntEnum('Option', *options)
        self.selected_option = 1

    def normalize_action(self, action) -> str:
        return action.split(':')[0].lower().replace(' ', '_')

    @has_sfx(sfx='swoosh', volume=SWOOSH_VOLUME)
    def call_method(self, action: str) -> None:
        action_name = self.normalize_action(action)

        method_name = f"perform_{action_name}"
        method = getattr(self.menu, method_name, None)

        if callable(method):
            method()
        else:
            raise AttributeError(f"Method {method_name} not found")
        self.menu.update_options_list()


    @has_sfx(sfx='swoosh', volume=SWOOSH_VOLUME)
    def update_selected_option(self, direction):
        self.selected_option = (((self.selected_option + direction - 1) % len(self.menu_option)) + 1)

    @property
    def selected_option_name(self) -> str:
        return self.menu_option(self.selected_option).name
