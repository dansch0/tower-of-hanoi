
import pygame


class Button:

    pressed = False

    def __init__(self, text, font, x, y, w, h, color, color_hovered, color_actived):
        self.text = text
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.color = color
        self.font = font
        self.color_hovered = color_hovered
        self.color_actived = color_actived

    def draw(self, game):

        clicked = False
        hovered = False
        active  = False

        # Checking button status
        rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

        if(rect.collidepoint(mouse_pos)):
            hovered = True
            
            if(mouse_down and not self.pressed):
                self.pressed = True
                active = True
            else:
                if(self.pressed):
                    clicked = True
                    self.pressed = False
                active = False
        else:
            self.pressed = False

        # Changing button collor
        button_color = self.color

        if(hovered):  button_color = self.color_hovered
        if(active):   button_color = self.color_actived

        # Drawing button
        game.render.render_rect(
            self.pos_x, 
            self.pos_y, 
            self.width, 
            self.height, 
            button_color)

        # Drawing text
        game.render.render_text_centered(
            self.text, 
            self.pos_x+(self.width/2), 
            self.pos_y+(self.height/2), 
            (255,255,255), 
            self.font)

        return clicked
        