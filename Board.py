import random

playerboard = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

user = 1

def print_the_board(playerboard):
    for i in playerboard:
        print(i)

print_the_board(playerboard) 

def check_piece(row, column):
    global playerboard
    if playerboard[row][column] != '-':
        return True
    else:
        return False
    
def tic_tac_toe():
    print_the_board(playerboard)
    turn()
    tic_tac_toe()

def turn():
    global user, playerboard
    invalid = True
    while invalid:
        print("Player " + str(user) + "'s turn")
        row = int(input("Row: "))
        column = int(input("Column: "))
        invalid = check_piece(row - 1, column - 1)
    if user == 1:
        playerboard[row-1][column-1] = "X"
    else:
        playerboard[row-1][column-1] = "O"
    if user == 2:
        user = 1
    else:
        user = 2

tic_tac_toe()
