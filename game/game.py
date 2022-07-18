
import time
import pygame

from game.event_manager import EventManager
from game.assets_manager import AssetsManager
from game.notification_manager import NotificationManager
from game.render_manager import RenderManager
from game.state_manager import StateManager

from game.constants import *

class Game:

    # If sets to true, the game closes
    quit_game = False

    # Window sizes
    WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
    
    # Window game title name
    WINDOW_TITLE = "Torre de Hanoi"

    GAME_FPS_CAP = 65

    rings_amount = 3

    username = "no_user"

    # Constructor
    def __init__(self):
        
        # ----- PyGame -----
        pygame.init()

        # ----- Initing our Render -----
        self.render = RenderManager(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # Setting the window title
        pygame.display.set_caption(self.WINDOW_TITLE)
        
        # Creating our Clock
        self.clock = pygame.time.Clock()

        # ----- Initing our Event Manager -----
        self.event_manager = EventManager()

        # ----- Loading all assets -----
        self.assets_manager = AssetsManager()

        # ----- Loading notifications -----    
        self.notification_manager = NotificationManager(self)

        # ----- Loading all states -----
        self.state_manager = StateManager(self)

        
    # Main loop
    def loop(self):

        # ----- Game events -----
        self.event_manager.update()

        # If the use click the close button...
        if(self.event_manager.CLOSE_GAME_BUTTON):
            self.quit_game = True

        # ----- Game states -----
        self.state_manager.update()

        # Rendering all notifications
        self.notification_manager.update()

        # ----- Window Render -----
        self.render.update_screen()

        # Limiting the frame rate
        self.clock.tick(self.GAME_FPS_CAP)

    # Disposing
    def quit(self):
        pygame.quit()