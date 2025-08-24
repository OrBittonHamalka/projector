import pygame
import random


def screen():
   background_colour = (51, 102, 0)
   screen = pygame.display.set_mode((800, 500))
   pygame.display.set_caption('The Flag')
   screen.fill(background_colour)
   pygame.display.flip()
   pygame.init()
   img = pygame.image.load('grass.png')
   IMAGE_SMALL = pygame.transform.scale(img, (50, 30))
   for position in range(20):
       rand_length = random.randint(0, 700)
       rand_width = random.randint(0, 400)
       screen.blit(IMAGE_SMALL, (rand_length, rand_width))
       pygame.display.flip()
       #לגרום לדשא לא להיות אחד על השני.
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False