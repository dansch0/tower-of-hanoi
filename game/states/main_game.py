
import pygame
from game.constants import *
from game.drag_manager import DragManager
from game.game_state import *
from game.states.main_menu import MainMenu


class MainGame(GameState):

    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        self.drag_manager = DragManager(game)

    def update(self):

        # Set background
        self.game.render.fill_screen(COLOR_BACKGROUND)

        # Get images
        ground_image = self.game.assets_manager.get_asset("Ground").asset_load
        bigbush_image = self.game.assets_manager.get_asset("BigBush").asset_load
        smallbush_image = self.game.assets_manager.get_asset("SmallBush").asset_load
        pole_image = self.game.assets_manager.get_asset("Pole").asset_load

        # Sizes
        ground_size_x, ground_size_y = ground_image.get_size()
        bigbush_size_x, bigbush_size_y = bigbush_image.get_size()
        pole_size_x, pole_size_y = pole_image.get_size()

        # Draw big bushes
        self.game.render.render_image(bigbush_image, 00, self.game.WINDOW_HEIGHT-ground_size_y-bigbush_size_y+12)

        # Draw small bushes
        self.game.render.render_image(smallbush_image, -20, self.game.WINDOW_HEIGHT-150)
        self.game.render.render_image(smallbush_image, self.game.WINDOW_WIDTH-320, self.game.WINDOW_HEIGHT-150)

        # Drawing ground
        self.game.render.render_image(ground_image, 0, self.game.WINDOW_HEIGHT-ground_size_y)

        # Drawing poles
        # Left
        self.game.render.render_image(pole_image, self.game.WINDOW_WIDTH/3-(self.game.WINDOW_WIDTH/6)-pole_size_x/2, self.game.WINDOW_HEIGHT-ground_size_y-pole_size_y+12)
        # Middle
        self.game.render.render_image(pole_image, self.game.WINDOW_WIDTH/2-pole_size_x/2, self.game.WINDOW_HEIGHT-ground_size_y-pole_size_y+12)
        # Right
        self.game.render.render_image(pole_image, (self.game.WINDOW_WIDTH/3-(self.game.WINDOW_WIDTH/6))*5-pole_size_x/2, self.game.WINDOW_HEIGHT-ground_size_y-pole_size_y+12)

        
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.game.state_manager.unpause_state(MainMenu)

        # Drag system
        self.drag_manager.update(self.game)

        font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load

        self.game.render.render_text(str(self.drag_manager.num_of_movements), 100, 100, (245, 245, 245), font_18)
        

        
        