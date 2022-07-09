

from random import randint
import time
import pygame


class DragItem:

    def __init__(self, item_size, image_name, game):
        
        self.draggable = False
        self.pressed = False
        self.pos_x = 0
        self.pos_y = 0
        self.click_timer = 0

        # Adding random positions to create a btf effect
        # when start game :)
        self.smooth_pos_x = randint(500*item_size, 500*item_size+500)
        self.smooth_pos_y = -randint(500*item_size, 500*item_size+500)
        if(item_size%2==0):
            self.smooth_pos_x = -self.smooth_pos_x
    

        self.game = game
        self.item_size = item_size
        self.item_image = game.assets_manager.get_asset(image_name).asset_load
        self.image_width = self.item_image.get_size()[0]
        self.image_height = self.item_image.get_size()[1]

    def check_first_click(self):

        mouse_down = pygame.mouse.get_pressed()[0]
        
        if(mouse_down):
            
            if(self.click_timer == 0):
                self.click_timer = time.time()

            how_long = time.time() - self.click_timer
            
            if(how_long <= 0):
                return True
            return False
        else:
            self.click_timer = 0

        return False
    
    def draw(self):

        active  = False
        dropped = False

        # Checking button status
        rect = pygame.Rect(self.pos_x, self.pos_y, self.image_width, self.image_height)
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]
        mouse_first_click = self.check_first_click()

        if(self.draggable):

            if(self.pressed and mouse_down):
                active = True
            elif(mouse_first_click):
                if(rect.collidepoint(mouse_pos)):
                    self.pressed = True
                    active = True
            else:
                if(self.pressed):
                    dropped = True
                self.pressed = False
            
        if(active):
            self.pos_x = mouse_pos[0] - self.image_width/2
            self.pos_y = mouse_pos[1] - self.image_height/2

        # Smoothing
        self.smooth_pos_x = self.smooth_pos_x-(self.smooth_pos_x-self.pos_x)/8
        self.smooth_pos_y = self.smooth_pos_y-(self.smooth_pos_y-self.pos_y)/8

        # Rendering the item
        self.game.render.render_image(self.item_image, self.smooth_pos_x, self.smooth_pos_y)

        return dropped

