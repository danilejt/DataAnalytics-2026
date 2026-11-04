# Mini-project #1: Tic tac Toe
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def display_board():
    
    print("")
    print("Current board:")
    print("*"*17)
    print(f"*   {board[0][0]} | {board[0][1]} | {board[0][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {board[1][0]} | {board[1][1]} | {board[1][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {board[2][0]} | {board[2][1]} | {board[2][2]}   *")
    print("*"*17)
    print()

def welcome_screen():
    print("Welcome to TIC TAC TOE!")
    print(" ")
    print("TIC TAC TOE")
    print("*"*17)
    print("*     |   |     *")
    print("*  ---|---|---  *")
    print("*     |   |     *")
    print("*  ---|---|---  *")
    print("*     |   |     *")
    print("*"*17)

def player_input(current_player):

    while True:
        row_input = int(input("Enter row: "))
        if row_input not in range (1,4):
            print("Invalid Row. Please type 1, 2, or 3.")
            continue
        
        column_input = int(input("Enter column: "))
        if column_input not in range (1,4):
            print ("Invalid column")
            continue

        row_index = row_input - 1
        column_index = column_input - 1
        entry = board[row_index][column_index]
                    
        if (entry) != " ": 
            print("The cell you have tried is already taken. Please try again")
            continue

        board[row_index][column_index] = current_player
        break

    if current_player == "X":
        current_player = "O"
    else: 
        current_player = "X"

    return current_player

def check_win(board, current_player):

    #checking rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            print(f"We have a winner, player {row[0]}")
            return True

    #checking columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != " ":
                print(f"We have a winner, player {board[0][column]}")
                return True

    #checking diagonal left
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f"We have a winner, player {board[0][0]}!")
        return True

    #checking diagonal right
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"We have a winner, player {board[0][2]}!")
        return True

    return False

def taiko():
    for row in board:
        if " " in row:
            return False;

    print("Cat's game")
    return True;

def play():
    welcome_screen()
    active_player = "X"

    while True:
        display_board()
        active_player = player_input(active_player)

        if check_win(board, active_player):
            display_board()
            print("thanks for having fun")
            break

        if taiko():
            display_board()
            break;
    
play()