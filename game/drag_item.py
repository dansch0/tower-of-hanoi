

import pygame


class DragItem:

    def __init__(self, item_size, image_name, game):
        
        self.pos_x = 0
        self.pos_y = 0
        self.smooth_pos_x = 0
        self.smooth_pos_y = 0
        self.draggable = False
        self.pressed = False

        self.game = game
        self.item_size = item_size
        self.item_image = game.assets_manager.get_asset(image_name).asset_load
        self.image_width = self.item_image.get_size()[0]
        self.image_height = self.item_image.get_size()[1]
    
    def draw(self):

        active  = False
        dropped = False

        # Checking button status
        rect = pygame.Rect(self.pos_x, self.pos_y, self.image_width, self.image_height)
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

        if(self.draggable):

            if(self.pressed and mouse_down):
                active = True
            elif(mouse_down):
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
        self.smooth_pos_x = self.smooth_pos_x-(self.smooth_pos_x-self.pos_x)/6
        self.smooth_pos_y = self.smooth_pos_y-(self.smooth_pos_y-self.pos_y)/6

        # Rendering the item
        self.game.render.render_image(self.item_image, self.smooth_pos_x, self.smooth_pos_y)

        return dropped

