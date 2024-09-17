class MenuActionHandlerMixin:
    def call_method(self, action: str) -> None:
        method_name = f"perform_{action}"
        method = getattr(self, method_name, None)
        if callable(method):
            method()
        else:
            raise AttributeError(f"Method {method_name} not found")
