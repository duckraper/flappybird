class ScenesStack:
    def __init__(self):
        self.stack: list['BaseScene'] = []

    def push(self, scene: 'BaseScene', stop_current=True):
        if stop_current:
            scene.stop_running()
        self.stack.append(scene)

    def pop(self, start_current=True) -> 'BaseScene':
        if len(self.stack) < 1:
            raise IndexError('pop() from empty scenes stack')

        scene = self.stack.pop()

        if start_current:
            scene.startup()

        return scene
