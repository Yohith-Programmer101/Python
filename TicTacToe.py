# TicTacToe.py

# In short:
# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagnols
# check tie
# flip player

# Code:
# -----Global Variable-----

# Game board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# if game still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it
current_player = "X"

# play game of tic tac toe
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def flip_player():
    return

def check_for_winner():
    # set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    columns_winner = check_columns()
    # check diagnols
    diagnol_winner = check_diagnols()

    # get the winner
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagnol_winner:
        winner = diagnol_winner
    else:
        winner = None
    return

def check_rows():
    # setup global variables
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # setup global variables
    global game_still_going
    columns_1 = board[0] == board[3] == board[6] != "_"
    columns_2 = board[1] == board[4] == board[7] != "_"
    columns_3 = board[2] == board[5] == board[8] != "_"
    # if any columns does have a match, flag that there is a win
    if columns_1 or columns_2 or columns_3:
        game_still_going = False
    # return the winner (X or O)
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return

def check_diagnols():
    # setup global variables
    global game_still_going
    diagnols_1 = board[0] == board[4] == board[8] != "_"
    diagnols_2 = board[6] == board[4] == board[2] != "_"
    # if any columns does have a match, flag that there is a win
    if diagnols_1 or diagnols_2 :
        game_still_going = False
    # return the winner (X or O)
    if diagnols_1:
        return board[0]
    elif diagnols_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()