from consts import ROWS, COLS, MINE, FLAG, PLAYER,FLAG_INDEX
import random
import pygame

from screen import start_screen


def create_empty_board ():
   board_matrix=[]
   for i in range (ROWS):
       row=[]
       for col in range (COLS):
           row.append("empty")
       board_matrix.append(row)
   return board_matrix
board_matrix=create_empty_board()


def add_player_flag ():
    row=0
    col=0
    for i in FLAG_INDEX:
        for j in i:
            if row==0:
                row=j
            else: col=j
        board_matrix[row][col]=FLAG
        row=0
        col=0
    board_matrix[0][0]=PLAYER
    return board_matrix
add_player_flag()


def add_mines ():
   board_matrix[0][0]=PLAYER
   counter=0
   used_ind = [[0, 0], FLAG_INDEX]
   while counter<20:
       put_together=[]
       random_row_ind=random.randint(0,24)
       random_col_ind=random.randint(0,49)
       put_together.append(random_row_ind)
       put_together.append(random_col_ind)
       if not put_together in used_ind:
           board_matrix[random_row_ind][random_col_ind]=MINE
           used_ind.append(put_together)
           counter+=1
   return board_matrix

add_mines()
# for i in board_matrix:
#     print(i,"\n")

# import pygame
#
# pygame.init()
# window = pygame.display.set_mode(((800, 600)))
# pygame.display.set_caption(('The Flag'))
#
# x, y = 50, 50
# width, height = 40, 60
# vel = 1
#
# clock = pygame.time.Clock()
# run = True
# while run:
#     clock.tick(100)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x -= vel
#     if keys[pygame.K_RIGHT]:
#         x += vel
#     if keys[pygame.K_UP]:
#         y -= vel
#     if keys[pygame.K_DOWN]:
#         y += vel
#
#     window.fill((0, 0, 0))
#     pygame.draw.rect(window, (200, 23, 255), (x, y, width, height))
#     pygame.display.update()
#
# pygame.quit()




