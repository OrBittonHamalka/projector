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
    while counter!=21:
        value=random.choice(board_matrix)
        if value!= "empty" or value!= FLAG:
            board_matrix.insert(board_matrix.index(value),MINE)
            counter+=1
    return board_matrix
add_flag_mines()
add_flag_mines()
print(board_matrix)
