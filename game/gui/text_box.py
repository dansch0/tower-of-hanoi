
import pygame


class TextBox:

    def __init__(self, game, x, y, w, h, color, font):
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.color = color
        self.font = font
        self.game = game
        self.text = ""
        self.selected = False

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
                        self.text += event.unicode

        #   --- Rendering --- 

        # Resizing the box if necessary
        text_size = self.game.render.get_text_size(self.text, self.font)
        input_width = self.width

        if(text_size[0] > self.width):
            input_width = text_size[0] + 20

        # Rectangle
        self.game.render.render_rect(self.pos_x, self.pos_y, input_width, self.height, (30, 30, 30))

        if(self.selected):
            self.game.render.render_rect(self.pos_x, self.pos_y, input_width, self.height, (150, 40, 40), 2)

        # Rendering the text
        self.game.render.render_text(self.text, self.pos_x+10, self.pos_y+text_size[1]/2, self.color, self.font)

        
        





