class MenuActionHandlerMixin:
    def call_method(self, action: str) -> None:
        action_name = action.lower().replace(' ', '_')

        method_name = f"perform_{action_name}"
        method = getattr(self, method_name, None)

        if callable(method):
            method()
        else:
            raise AttributeError(f"Method {method_name} not found")
