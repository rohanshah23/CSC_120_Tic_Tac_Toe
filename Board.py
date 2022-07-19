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
    result = game_result(playerboard)
    if result == "X":
        print("User 1 won")
    elif result == "O":
        print("User 2 won")
      
        
        
    tic_tac_toe()

def turn():
    global user, playerboard
    invalid = True
    while invalid:
        print("User " + str(user) + "'s turn")
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
        
        
def game_result(playerboard):
    for i in range(3):
        if len(set(playerboard[i])) == 1:
            return playerboard[i][0]
    for x in range(3):
        if len(set([i[x] for i in playerboard])) == 1:
            return playerboard[0][x]
    if playerboard[0][0] == playerboard[1][1] == playerboard[2][2] or playerboard[0][2] == playerboard[1][1] == playerboard[2][0]:
        return playerboard[1][1]
        

tic_tac_toe()

    
