import pygame

class Gui:
    width = 1000
    height = 800
    running = True

    @classmethod
    def init(cls):
        pygame.init()

        cls.clock = pygame.time.Clock()

        cls.screen = pygame.display.set_mode((cls.width, cls.height))