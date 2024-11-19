import pygame

class GameWindow:
    def __init__(self):
        self.running = True
        self.size = self.width, self.height = 640, 400
        self.clock = pygame.time.Clock()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def loop(self):
        self.screen.fill("purple")

    def render(self):
        pygame.display.flip()
        self.clock.tick(60)
    
    #initilizes the window
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

    #quits the window
    def cleanup(self):
        pygame.quit()

    #starts the gameloop
    def execute(self):
        
        self.init()

        while self.running:
            self.event()
            self.loop()
            self.render()
        
        self.cleanup()
