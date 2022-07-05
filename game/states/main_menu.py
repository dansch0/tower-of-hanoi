
import pygame
from game.constants import *
from game.game_state import *


class MainMenu(GameState):

    def __init__(self, type, game):
        GameState.__init__(self, type, game)

    def update(self):

        # Get assets
        font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load

        self.game.render.fill_screen(COLOR_BLACK)

        self.game.render.render_text("Main menu", 100, 100, (100, 200, 70), font_18)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.game.state_manager.pause_state(MainMenu)