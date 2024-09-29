class ScenesStack:
    def __init__(self):
        self.stack: list['BaseScene'] = []

    def push(self, scene: 'BaseScene'):
        self.stack.append(scene)

    def pop(self) -> 'BaseScene':
        if len(self.stack) < 1:
            raise IndexError('pop() from empty scenes stack')

        return self.stack.pop()
