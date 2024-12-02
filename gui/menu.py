import pygame
from gui.gui import Gui

class Menu:
    
    i = 0

    button = pygame.Surface((100, 100))
    button.fill("blue")

    button2 = pygame.Surface((100,100))
    button2.fill("red")
    
    @classmethod
    def blit(cls):
        pygame.Surface.blit(Gui.screen, cls.button, (cls.i,cls.i))
        pygame.Surface.blit(Gui.screen, cls.button2, (600-cls.i, 600-cls.i))
        cls.i += 1