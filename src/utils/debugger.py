import pygame as pg

class Debug:
    def __init__(self, info: any='None', x: int=15, y: int=15,  **kwargs):
        self.font_color: str | tuple[int, int, int] = kwargs.get('font_color', 'black')
        self.bg_color: str | tuple[int, int, int] = kwargs.get('bg_color', 'white')
        self.info: str = info
        self.display_surface: pg.Surface = pg.display.get_surface()

        self.font: pg.font.Font = pg.font.Font(None, 30)
        self.image: pg.Surface = self._render_image()
        self.rect: pg.Rect = self.image.get_rect(topleft=(x, y))
        pg.draw.rect(self.display_surface, self.bg_color, self.rect, width=0)
    
    def draw(self, *args, **kwargs):
        self.update(*args, **kwargs)
        self.display_surface.blit(self.image, self.rect)

    def update(self, *args, **kwargs):
        if 'info' in kwargs:
            self.info = kwargs['info']
            self.image = self._render_image()

    def _render_image(self):
        return self.font.render(str(self.info), True, self.font_color)
