
import time
from tkinter import NORMAL
from game.constants import COLOR_WHITE


class NotificationColor:
    GREEN = (106, 176, 76)
    RED = (192, 57, 43)
    BLUE = (41, 128, 185)
    YELLOW = (241, 196, 15)

class NotificationPosition:
    TOP = 0
    CENTER = 1

class NotificationType:
    NORMAL = 0
    BIG = 1


class Notification:

    def __init__(
            self, 
            text,
            game,
            duration_time = 3.5, # One second
            color=NotificationColor.GREEN, 
            position = NotificationPosition.TOP,
            type = NotificationType.NORMAL
        ) -> None:
        
        self.finished = False
        self.text = text
        self.game  = game
        self.duration_time = duration_time
        self.color = color
        self.position = position
        self.type = type    
        self.timer = 0

        self.pos_x = game.WINDOW_WIDTH/2
        self.pos_y = 0

        # Get font
        self.font = None
        
        if(type == NotificationType.NORMAL):
            self.font = game.assets_manager.get_asset("PixelFont14").asset_load
            
        elif(type == NotificationType.BIG):
            self.font = game.assets_manager.get_asset("PixelFont32").asset_load

        # Get text rect
        self.text_x, self.text_y = game.render.get_text_size(text, self.font)

        # Setting text start pos
        self.start_pos_y = -50
        self.end_pos_y = 0

        if(position == NotificationPosition.TOP):
            self.end_pos_y = self.text_y + 50

        elif(position == NotificationPosition.CENTER):
            self.end_pos_y = game.WINDOW_HEIGHT/2   

        # Initing smooth vars
        self.smooth_pos_x = game.WINDOW_WIDTH/2
        self.smooth_pos_y = -50


    def draw(self):
        
        # Getting time
        if(self.timer == 0):
            self.timer = time.time()

        finished_animation = (time.time() - self.timer >= self.duration_time)

        if(finished_animation):
            self.pos_y = self.start_pos_y
        else:
            self.pos_y = self.end_pos_y
        
        # Check if we end the animation
        if(finished_animation and self.smooth_pos_y//2 == self.pos_y//2):
            self.finished = True

        # Smoothing
        self.smooth_pos_x = self.smooth_pos_x-(self.smooth_pos_x-self.pos_x)/8
        self.smooth_pos_y = self.smooth_pos_y-(self.smooth_pos_y-self.pos_y)/8
        
        padding = 15

        self.game.render.render_rect(
            self.smooth_pos_x-(self.text_x/2)-padding, 
            self.smooth_pos_y-(self.text_y/2)-padding, 
            self.text_x+(padding*2), 
            self.text_y+(padding*2), 
            self.color)

        # Rendering text
        self.game.render.render_text_centered(
            self.text, 
            self.smooth_pos_x, 
            self.smooth_pos_y, 
            COLOR_WHITE, 
            self.font)