
import pygame

class RenderManager:

    def __init__(self, window_width, window_height):
        # Creating Window
        self.screen = pygame.display.set_mode((window_width, window_height))

    def update_screen(self):
        pygame.display.flip()

    def render_image(self, image, x, y):
        self.screen.blit(image, (x, y))

    def fill_screen(self, color):
        self.screen.fill(color)

    def render_text(self, text, x, y, color, font):
        text_surface = font.render(text, False, color)
        self.screen.blit(text_surface, (x,y))