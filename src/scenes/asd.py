import pygame as pg
from resources import screen, screen_width, screen_height, colors, font_size, script_directory, game_title
from pathlib import Path

class MainMenu:
    def __init__(self):
        self.running = True

        self.title_font = pg.font.Font(script_directory.joinpath("data", "fonts","Pixeled.ttf"), font_size + font_size//3)
        self.option_font = pg.font.Font(script_directory.joinpath(
            "data", "fonts", "Pixeled.ttf"), font_size - font_size//3)

        self.menu_options = ["Iniciar Juego", "Opciones", "Creditos", "Salir"]
        self.selected_option = 0

    def get_input(self):
        key = pg.key.get_pressed()

        if key[pg.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)

        elif key[pg.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)


    def draw_menu(self):
        title_text = self.title_font.render(game_title, True, colors['white'])
        title_rect = title_text.get_rect(center=(screen_width// 2, screen_height // 4))

        screen.blit(title_text, title_rect)

        for i, option in enumerate(self.menu_options):
            option_color = colors['gray'] if i == self.selected_option else colors['white']
            option_text = self.option_font.render(option, True, option_color)
            option_rect = option_text.get_rect(
                center=(screen_width// 2, screen_height // 2 + i * 60))
            screen.blit(option_text, option_rect)

