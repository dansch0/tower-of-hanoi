
import pygame

class EventManager:

    # Game buttons pressed
    CLOSE_GAME_BUTTON = False

    def __init__(self):
        print("Event manager start")

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.CLOSE_GAME_BUTTON = True

