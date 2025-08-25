import sys
import game_field
import pygame
import random

from game_field import board_matrix

image_flag = pygame.image.load("flag.png") #uploading pictures
image_mine = pygame.image.load("mine.png")
image_grass = pygame.image.load('grass.png')
image_soldier = pygame.image.load("soldier.png")
image_soldier_night = pygame.image.load("soldier_nigth.png")
line_color = (200, 200, 200) #determining line colors for night vision
block_size = 10 ##determining square size for night vision
IMAGE_SMALL = pygame.transform.scale(image_grass, (50, 30))
listn = []


def define_screen():
   global screen
   background_colour = (51, 102, 0)
   screen = pygame.display.set_mode((800, 600)) #screen size
   pygame.display.set_caption('The Flag') #naming the window
   screen.fill(background_colour)
   pygame.display.flip()
   pygame.init()

def randomize_grass():
   for position in range(20): #adding 20 grass pics on the screen randomly
       rand_length = random.randint(0, 700)
       rand_width = random.randint(0, 500)
       listn.append(rand_length)
       listn.append(rand_width)
       set(listn)
       screen.blit(IMAGE_SMALL, (rand_length, rand_width))
       pygame.display.flip()

def enter_pic_soldier():
    small_soldier = pygame.transform.scale(image_soldier, (80, 80)) #sizing down the soldier
    screen.blit(small_soldier, (0,0)) #adding the soldier

def enter_pic_flag():
   small_flag = pygame.transform.scale(image_flag, (50, 50))
   screen.blit(small_flag, (748, 548))

def write_greeting():
    font = pygame.font.SysFont("Arial", 20)
    welcome = font.render("Welcome to The Flag game.", True, (255, 255, 255))
    have_fun = font.render("Have Fun!", True, (255, 255, 255))
    text_rect = welcome.get_rect(center=(200, 20))
    text_rect1 = have_fun.get_rect(center=(135, 40))
    screen.blit(welcome, text_rect)
    screen.blit(have_fun, text_rect1)
    pygame.display.flip()

def game_running():
   running = True #the window doesn't close until the user closes it
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False

