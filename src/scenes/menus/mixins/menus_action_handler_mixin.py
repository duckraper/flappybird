from src.commons.audio_player import AudioPlayer
from src.commons.constants import SWOOSH_VOLUME


class MenuActionHandlerMixin:
    def call_method(self, action: str) -> None:
        action_name = action.lower().replace(' ', '_')

        method_name = f"perform_{action_name}"
        method = getattr(self, method_name, None)

        if callable(method):
            method()
            AudioPlayer.play_sound('swoosh', SWOOSH_VOLUME)
        else:
            raise AttributeError(f"Method {method_name} not found")
