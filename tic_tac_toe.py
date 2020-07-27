from os import system, name
import random

def clear_output():
	if name == 'nt': _ = system('cls')
	else: _ = system('clear')

def display_board(board):
    clear_output()
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(board[0], board[1], board[2]))
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(board[3], board[4], board[5]))
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  {}  |  {}  |  {} ".format(board[6], board[7], board[8]))
    print("     |     |     ")

def player_input():
    flag = True
    while flag:
        m1 = input("Hey Player 1, Choose your Marker - X or O  : ")
        if m1.lower() == 'x':
            print("Hey Player 2, Your Marker is : O")
            m2 = 'O'
            flag = False
        elif m1.lower() == 'o':
            print("Hey Player 2, Your Marker is : X")
            m2 = 'X'
            flag = False
        else:
            clear_output()
            print("Kindly Choose between O or X\n\n\n")
    return (m1.upper(), m2.upper())

def place_marker(board, marker, position):
    board[position-1] = marker.upper()

def win_check(board, mark):
    mark = mark.upper()
    # First 3 Rows
    if mark == board[0] and mark == board[1] and mark == board[2]: return True
    elif mark == board[3] and mark == board[4] and mark == board[5]: return True
    elif mark == board[6] and mark == board[7] and mark == board[8]: return True
    # First 3 Columns
    elif mark == board[0] and mark == board[3] and mark == board[6]: return True
    elif mark == board[1] and mark == board[4] and mark == board[7]: return True
    elif mark == board[2] and mark == board[5] and mark == board[8]: return True
    # 2 Diagonals
    elif mark == board[0] and mark == board[4] and mark == board[8]: return True
    elif mark == board[2] and mark == board[4] and mark == board[6]: return True
    else: return False

def space_check(board, position):
    if board[position-1] == " ": return True
    else: return False

def full_board_check(board):
    if " " in board: return False
    else: return True

def player_choice(board, turn):
    flag = True
    while flag:
        pos = int(input(turn + " Enter a Position:  "))
        check = space_check(board,pos)
        if check == True: return pos
        else: print("Place is already Filled!\n")

def replay():
    sel = input("Do You Want to Play Again? ")
    if sel.lower() == 'yes': return True
    else: return False

def choose_first():
    if random.randint(0, 1) == 0: return 'Player 2'
    else: return 'Player 1'

print("Welcome To Tic Tac Toe")
while True:
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('\n\n' + turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')
    if play_game.lower()[0] == 'y': game_on = True
    else: game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board, turn)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 has Won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('This Game is a Draw!')
                    break
                else: turn = 'Player 2'

        else:
            display_board(board)
            position = player_choice(board, turn)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has Won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('This Game is a Draw!')
                    break
                else: turn = 'Player 1'
    if not replay(): break
