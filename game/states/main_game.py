
import pygame
from game.constants import *
from game.drag_manager import DragManager
from game.game_state import *
from game.notification import Notification
from game.notification_manager import NotificationManager
from game.states.main_menu import MainMenu


class MainGame(GameState):

    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

        self.drag_manager = DragManager(game)

        self.loaded_notifications = False

    def update(self):

        if(not self.loaded_notifications):
            self.game.notification_manager.add_notification(Notification("Para ganhar o jogo você deve empilhar todo os anéis em um pino diferente.", self.game))
            self.game.notification_manager.add_notification(Notification(f"Boa sorte, {self.game.username}!", self.game))
            self.loaded_notifications = True

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

        # Drag system
        self.drag_manager.update(self.game)

        font_18 = self.game.assets_manager.get_asset("PixelFont18").asset_load
        movements_text = str(self.drag_manager.num_of_movements)
        text_size = self.game.render.get_text_size(movements_text, font_18)

        self.game.render.render_rect(self.game.WINDOW_WIDTH/2-text_size[0]/2-15, 100, text_size[0]+30, 40, COLOR_BACKGROUND_LIGHT)
        self.game.render.render_text_centered(str(self.drag_manager.num_of_movements), self.game.WINDOW_WIDTH/2, 120, (245, 245, 245), font_18)


        
        

        
        