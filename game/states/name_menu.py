
from game.game_state import GameState

import pygame
from game.constants import *
from game.game_state import *
from game.gui.button import Button
from game.gui.text_box import TextBox
from game.notification import *


class NameMenu(GameState):
    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        # Get assets
        self.font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load

        # Initing all buttons
        self.ok_button = Button(
            "OK",
            self.font_18, 
            640-125, 380, 
            250, 60, 
            COLOR_MAIN,
            COLOR_MAIN_DARK,  
            COLOR_MAIN_DARKER)

        self.name_box = TextBox(
            game, 
            game.WINDOW_WIDTH/2-(500/2), 280, 
            500, 40, 
            self.font_18,
            limit=24,
            bg_color=COLOR_BACKGROUND_LIGHT, 
            selected_color=COLOR_MAIN
            )

    def update(self):

        self.game.render.fill_screen(COLOR_BACKGROUND_MENU)

        font18 = self.game.assets_manager.get_asset("PixelFont18").asset_load
        font24 = self.game.assets_manager.get_asset("PixelFont24").asset_load
        self.game.render.render_text_centered("Quem é?", 640, 160, (245, 245, 245), font24)
        self.game.render.render_text_centered("Digite seu nome por favor:", 640, 220, (245, 245, 245), font18)

        if(self.ok_button.draw(self.game)):
            text = self.name_box.text.strip()
            if(text == ""):
                self.game.notification_manager.add_notification(Notification(
                    "Digite seu nome!",
                    self.game,
                    color=NotificationColor.RED, 
                ))
            elif(len(text) < 3):
                self.game.notification_manager.add_notification(Notification(
                    "Que nome pequeno... Digite um nome maior!",
                    self.game,
                    color=NotificationColor.RED, 
                ))
            else:
                self.game.username = text.title()
                self.game.state_manager.pause_state(NameMenu)

        self.name_box.draw()