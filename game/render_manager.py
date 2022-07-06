
import pygame

class RenderManager:

    def __init__(self, window_width, window_height):
        # Creating Window
        self.screen = pygame.display.set_mode((window_width, window_height))

    def update_screen(self):
        pygame.display.flip()

    def render_rect(self, x, y, w, h, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, w, h))

    def render_image(self, image, x, y):
        self.screen.blit(image, (x, y))

    def fill_screen(self, color):
        self.screen.fill(color)

    def render_text(self, text, x, y, color, font):
        text_surface = font.render(text, False, color)
        self.screen.blit(text_surface, (x,y))
    
    def render_text_centered(self, text, x, y, color, font):
        text = font.render(text, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)