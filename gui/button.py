import pygame
from gui.gui import Gui

class Button():
    def __init__(self, rect, color):
        self.button_rect = pygame.Rect(rect)

        self.button = pygame.Surface((self.button_rect.width, self.button_rect.height))
        self.button.fill(color)

    def blit(self):
        pygame.Surface.blit(Gui.screen, self.button, self.button_rect)