import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board(): 
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #going to make a matrix with all zeros with 6 rows by 7 columns 
    return board

# prints out the board in the terminal 
# board = create_board()
# print(board)

def drop_piece(board, row, column, piece):
    board[row][column] = piece

def is_valid_location(board, column): 
    return board[ROW_COUNT-1][column] == 0 

def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r

def print_board(board): # flips the board over to print out correctly 
    print(np.flip(board, 0))

def winning_move(board): # Going to build my own algorithm 
    pass

board = create_board()
print_board(board)
game_over = False #the only way this is going to True is if someone got 4 in a row. 
turn = 0

while not game_over: 
    # Ask for Player 1 Input
    if turn == 0:
        column = int(input("Player 1 Make your Selection (0-6):"))

        # print(selection)
        # print(type(selection)) # checked to see what data type it was printing out. 
        # It was printing as a string so the int() went in front of the input 

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

    # Ask for Player 2 Input
    else: 
        column = int(input("Player 2 Make your Selection (0-6):"))

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)
        
    print_board(board)

    turn += 1 
    turn = turn % 2 # line 29 and 30 is so that the secletion alternates between turns (player 1 and player 2). 
    #Because we turned the input into an int we have to do a little math.

# had to change the python version in the left bottom corner. 
# https://medium.com/@syarif.secondchance/vs-code-python-unresolved-import-warning-ea9bba3fa9af