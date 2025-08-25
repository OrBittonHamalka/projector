import sys
import game_field
import pygame
import random

pygame.init()

image_flag = pygame.image.load("flag.png")
image_mine = pygame.image.load("mine.png")
image_grass = pygame.image.load("grass.png")
image_soldier = pygame.image.load("soldier.png")

IMAGE_SMALL = pygame.transform.scale(image_grass, (50, 30))
clock = pygame.time.Clock()
FPS = 60
s_width, s_height = 800, 600

grass_positions = []

def define_screen():
    global screen, small_flag, font, welcome, have_fun, text_rect, text_rect1
    screen = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('The Flag')
    for _ in range(20):
        rand_length = random.randint(0, 700)
        rand_width = random.randint(0, 500)
        grass_positions.append((rand_length, rand_width))
    small_flag = pygame.transform.scale(image_flag, (50, 50))

    font = pygame.font.SysFont("Arial", 20)
    welcome = font.render("Welcome to The Flag game.", True, (255, 255, 255))
    have_fun = font.render("Have Fun!", True, (255, 255, 255))
    text_rect = welcome.get_rect(center=(200, 20))
    text_rect1 = have_fun.get_rect(center=(135, 40))

def enter_pic_soldier():
    global char_rect, small_soldier
    small_soldier = pygame.transform.scale(image_soldier, (80, 80))
    char_rect = small_soldier.get_rect()
    char_rect.topleft = (0, 0)

def draw_background():
    screen.fill((51, 102, 0))
    for pos in grass_positions:
        screen.blit(IMAGE_SMALL, pos)
    screen.blit(small_flag, (748, 548))
    screen.blit(welcome, text_rect)
    screen.blit(have_fun, text_rect1)

def game_running():
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            char_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            char_rect.x += 5
        if keys[pygame.K_UP]:
            char_rect.y -= 5
        if keys[pygame.K_DOWN]:
            char_rect.y += 5

        if char_rect.left < 0:
            char_rect.left = 0
        if char_rect.right > s_width:
            char_rect.right = s_width
        if char_rect.top < 0:
            char_rect.top = 0
        if char_rect.bottom > s_height:
            char_rect.bottom = s_height

        draw_background()
        screen.blit(small_soldier, char_rect)
        pygame.display.flip()
