
from game.game_state import GameState

import pygame
from game.constants import *
from game.game_state import *
from game.gui.button import Button
from game.states.main_game import MainGame


class DifficultyMenu(GameState):
    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        # Get assets
        self.font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load

        # Initing all buttons
        self.ring3 = Button(
            "3",
            self.font_18, 
            640/4-125, 360, 
            100, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

        self.ring4 = Button(
            "4",
            self.font_18, 
            640/4*2-125, 360, 
            100, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

        self.ring5 = Button(
            "5",
            self.font_18, 
            640/4*3-125, 360, 
            100, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

        self.ring6 = Button(
            "6",
            self.font_18, 
            640/4*4-125, 360, 
            100, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

    def update(self):

        # Set background
        self.game.render.fill_screen(COLOR_BACKGROUND)

        font = self.game.assets_manager.get_asset("PixelFont18").asset_load
        self.game.render.render_text_centered("Escolha a quantidade de anéis para jogar", 640, 200, (245, 245, 245), font)
        self.game.render.render_text_centered("Quanto mais anéis mais difícil é ;)", 640, 250, (245, 245, 245), font)

        choice_number = 0

        if(self.ring3.draw(self.game)):
            choice_number = 3
        if(self.ring4.draw(self.game)):
            choice_number = 4
        if(self.ring5.draw(self.game)):
            choice_number = 5
        if(self.ring6.draw(self.game)):
            choice_number = 6

        if(choice_number != 0):
            self.game.rings_amount = choice_number
            self.game.state_manager.pause_state(DifficultyMenu)
            self.game.state_manager.reset_state(MainGame(GameStateType.SOLID, self.game))
            