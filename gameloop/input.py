from gui.gui import Gui
import pygame

class Input():
    
    @classmethod
    def execute(cls):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Gui.running = False
        
        #cls.user_input = input()

        
        