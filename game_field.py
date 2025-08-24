from consts import ROWS,COLS,MINE,FLAG
import random


def create_empty_board ():
   board_matrix=[]
   for i in range (ROWS):
       row=[]
       for col in range (COLS):
           row.append("empty")
       board_matrix.append(row)
   return board_matrix
board_matrix=create_empty_board()


def add_flag_mines ():
   board_matrix[24][49]=FLAG
   counter=0
   used_ind = [[0, 0], [24, 49]]
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




add_flag_mines()
print(board_matrix)
