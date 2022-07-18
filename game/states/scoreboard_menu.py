
from game.game_state import GameState

import pygame
from game.constants import *
from game.game_state import *
from game.gui.button import Button

class ScoreboardMenu(GameState):
    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        self.font_14 = self.game.assets_manager.get_asset("PixelFont14").asset_load

        self.back_button = Button(
            game,
            "Voltar",
            self.font_14, 
            640-60, 600, 
            120, 40, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

    def update(self):
        
        # Set background
        self.game.render.fill_screen(COLOR_BACKGROUND)

        font = self.game.assets_manager.get_asset("PixelFont18").asset_load
        self.game.render.render_text_centered("Top 10 jogadores", 640, 100, (245, 245, 245), font)

        if(self.back_button.draw()):
            self.game.state_manager.pause_state("ScoreboardMenu")
            self.game.state_manager.unpause_state("MainMenu")
