
import pygame

from game.constants import *


class TextBox:

    def __init__(self, game, x, y, w, h, font, limit=0, bg_color=COLOR_BLACK, text_color=COLOR_WHITE, selected_color=COLOR_RED):
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.text_color = text_color
        self.bg_color = bg_color
        self.selected_color = selected_color
        self.font = font
        self.limit = limit
        self.game = game
        self.text = ""
        self.selected = False

        self.blacklist_keys = [pygame.K_RETURN]

    def is_valid_key(self, key):
        for key_ in self.blacklist_keys:
            if(key == key_):
                return False

        return True

    def draw(self):
        
        rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        mouse_pos = pygame.mouse.get_pos()
        mouse_first_click = self.game.event_manager.MOUSE_LEFT_CLICK
        mouse_hover_box = rect.collidepoint(mouse_pos)

        #   --- Events ---
        # check click
        if(mouse_first_click):
            if(mouse_hover_box):
                self.selected = True
            else:
                self.selected = False 

        # keyboard events
        if(self.selected):
            
            for event in self.game.event_manager.events_pack:
                if(event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]
                    else:
                        if(not self.is_valid_key(event.key)):
                            continue

                        if(self.limit > 0 and len(self.text) == self.limit):
                            continue

                        self.text += event.unicode

        #   --- Rendering --- 

        # Resizing the box if necessary
        text_size = self.game.render.get_text_size(self.text, self.font)
        input_width = self.width

        if(text_size[0] > self.width):
            input_width = text_size[0] + 20

        # Rectangle
        self.game.render.render_rect(self.pos_x, self.pos_y, input_width, self.height, self.bg_color)

        if(self.selected):
            self.game.render.render_rect(self.pos_x, self.pos_y, input_width, self.height, self.selected_color, 2)

        # Rendering the text
        self.game.render.render_text(self.text, self.pos_x+10, self.pos_y+text_size[1]/2, self.text_color, self.font)

        
        





