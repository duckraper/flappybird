class BGManager:
    def __init__(self, scene):
        self.scene: 'BaseScene' = scene
        self.bg = None

    def set_bg(self, bg: 'Background'):
        self.bg = bg
        self.scene.add(self.bg)

    def update(self):
        self.bg.update()
