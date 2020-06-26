import numpy as np 

def create_board(): 
    board = np.zeros((6,7)) #going to make a matrix with all zeros with 6 rows by 7 columns 
    return board

# prints out the board in the terminal 
# board = create_board()
# print(board)


board = create_board()
game_over = False #the only way this is going to True is if someone got 4 in a row. 
turn = 0

while not game_over: 
    # Ask for Player 1 Input
    if turn == 0:
        selection = int(input("Player 1 Make your Selection (0-6):"))

        # print(selection)
        # print(type(selection)) # checked to see what data type it was printing out. 
        # It was printing as a string so the int() went in front of the input 

    # Ask for Player 2 Input
    else: 
        selection = int(input("Player 2 Make your Selection (0-6):"))

    turn += 1 
    turn = turn % 2

# had to change the python version in the left bottom corner. 
# https://medium.com/@syarif.secondchance/vs-code-python-unresolved-import-warning-ea9bba3fa9af