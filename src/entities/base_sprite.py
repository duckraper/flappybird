import pygame as pg

class BaseSprite(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, x: int, y: int):
        super().__init__()
        self.image: pg.Surface = image
        self.rect: pg.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
