
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

        font18 = self.game.assets_manager.get_asset("PixelFont18").asset_load
        font14 = self.game.assets_manager.get_asset("PixelFont14").asset_load
        self.game.render.render_text_centered("Top 10 jogadores", 640, 80, (245, 245, 245), font18)

        # Rendering the scores tables
        score_text_width = 305
        score_text_pos_x = 50

        for i in range(0, 4):
            
            num_of_rings = i+3

            # Top title, num of rings
            self.game.render.render_text(f"{num_of_rings} anéis", score_text_pos_x, 160, COLOR_YELLOW, font18)

            # Getting data
            scores = self.game.config_manager.get_score_by_rings_amount(num_of_rings)

            score_text_pos_y = 200

            if(len(scores) == 0):
                self.game.render.render_text("Ninguém jogou.", score_text_pos_x, score_text_pos_y, (100, 100, 100), font14)
                score_text_pos_x += score_text_width
                continue

            for score in scores:
                score_name = score[0]
                score_number = score[1]

                self.game.render.render_text(score_name,    score_text_pos_x,       score_text_pos_y, (245, 245, 245), font14)
                self.game.render.render_text_right(str(score_number),  score_text_pos_x+score_text_width-40,   score_text_pos_y, (245, 245, 245), font14)

                score_text_pos_y += 25
            
            score_text_pos_x += score_text_width

        if(self.back_button.draw()):
            self.game.state_manager.pause_state("ScoreboardMenu")
            self.game.state_manager.unpause_state("MainMenu")
