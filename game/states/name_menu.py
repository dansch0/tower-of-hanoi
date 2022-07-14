
from game.game_state import GameState

import pygame
from game.constants import *
from game.game_state import *
from game.gui.button import Button
from game.gui.text_box import TextBox


class NameMenu(GameState):
    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        # Get assets
        self.font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load

        # Initing all buttons
        self.ok_button = Button(
            "OK",
            self.font_18, 
            640-125, 500, 
            250, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

        self.name_box = TextBox(
            game, 
            game.WINDOW_WIDTH/2-(400/2), 360, 
            400, 40, 
            COLOR_WHITE, 
            self.font_18)

    def update(self):

        self.game.render.fill_screen(COLOR_BACKGROUND_MENU)

        font = self.game.assets_manager.get_asset("PixelFont18").asset_load
        self.game.render.render_text_centered("Quem é?", 640, 200, (245, 245, 245), font)
        self.game.render.render_text_centered("Digite seu nome por favor:", 640, 220, (245, 245, 245), font)

        if(self.ok_button.draw(self.game)):
            self.game.username = self.name_box.text
            self.game.state_manager.pause_state(NameMenu)

        self.name_box.draw()