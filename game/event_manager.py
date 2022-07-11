
import pygame

class EventManager:

    CLOSE_GAME_BUTTON = False
    MOUSE_LEFT_CLICK = False

    def __init__(self):
        print("Event manager start")

    def update(self):

        self.MOUSE_LEFT_CLICK = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.CLOSE_GAME_BUTTON = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.MOUSE_LEFT_CLICK = True

