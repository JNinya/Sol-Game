import pygame


width = 1000
height = 600
running = True

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

surface = pygame.Surface((width, height))

surface.fill("blue")

i = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")
    
    pygame.Surface.blit(screen, surface, (i, 100))

    i+=1

    pygame.display.flip()

    clock.tick(60)