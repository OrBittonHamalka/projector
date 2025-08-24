from consts import ROWS,COLS,MINE,FLAG
import random

def creat_empty_board ():
    board_matrix=[]
    for i in range (ROWS):
        row=[]
        for col in range (COLS):
            row.append("empty")
        board_matrix.append(row)
    return board_matrix
board_matrix=creat_empty_board()

def add_flag_mines ():
    board_matrix[24][49]=FLAG
    return board_matrix
    counter=0
    while counter!=21:
        value=random.choice(board_matrix)
        if value!= "empty":
            value=MINE
add_flag_mines()
print(board_matrix)
