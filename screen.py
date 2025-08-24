import pygame

def screen():
    background_colour = (51, 102, 0)
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('The Flag')
    screen.fill(background_colour)
    pygame.display.flip()
    pygame.init()
    img = pygame.image.load('grass.png')
    IMAGE_SMALL = pygame.transform.scale(img, (50, 30))
    running = True
    while running:
        screen.blit(IMAGE_SMALL, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
