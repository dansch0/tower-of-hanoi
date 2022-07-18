
import pygame
from game.constants import *
from game.game_state import *
from game.gui.button import Button
from game.notification import Notification
from game.states.scoreboard_menu import ScoreboardMenu


class MainMenu(GameState):

    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        self.loaded_notifications = False

        # Get assets
        self.font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load

        # Initing all buttons
        self.start_button = Button(
            game,
            "INICIAR",
            self.font_18, 
            640-125, 360-80, 
            250, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

        self.score_button = Button(
            game,
            "PLACAR",
            self.font_18, 
            640-125, 360, 
            250, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

        self.exit_button = Button(
            game,
            "SAIR",
            self.font_18, 
            640-125, 360+80, 
            250, 60, 
            (200, 100, 30),
            (190, 90, 20),  
            (170, 80, 20))

    def update(self):

        if(not self.loaded_notifications):
            self.game.notification_manager.add_notification(Notification(f"Bem-vindo, {self.game.username}!", self.game))
            self.loaded_notifications = True

        self.game.render.fill_screen(COLOR_BACKGROUND_MENU)

        font_32 = self.game.assets_manager.get_asset("PixelFont32").asset_load
        self.game.render.render_text_centered("HANOI'S TOWER", 640, 200, (245, 245, 245), font_32)

        if(self.start_button.draw()):
            self.game.state_manager.pause_state("MainMenu")
            self.game.state_manager.unpause_state("DifficultyMenu")

        if(self.score_button.draw()):
            self.game.state_manager.unpause_state("ScoreboardMenu")

        if(self.exit_button.draw()):
            self.game.quit_game = True
            