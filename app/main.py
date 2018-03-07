import random

#Take Player input
def player_input():
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = raw_input('Enter marker for Player 1: ')
    player2 = 'O' if player1 == 'X' else 'X'
    return (player1, player2)

#Place mark and update board
def update_place_mark(pos, playerMark, board):
    board[pos] = playerMark
    display_board(board)

#Print board
def display_board(board):
        print ('{ ' + board[7] + ' }' + '||' + '{ ' +board[8] + ' }' + '||' + '{ ' + board[9] + ' }')
        print ('{ ' + board[4] + ' }' + '||' + '{ ' +board[5] + ' }' + '||' + '{ ' + board[6] + ' }')
        print ('{ ' + board[1] + ' }' + '||' + '{ ' +board[2] + ' }' + '||' + '{ ' + board[3] + ' }')

#Check if player wins
def check_winner(board, marker):
    won = False
    if (board[7] == board[8] == board[9] == marker) \
            or (board[1] == board[2] == board[3] == marker) \
            or (board[4] == board[5] == board[6] == marker) \
            or (board[1] == board[4] == board[7] == marker) \
            or (board[3] == board[6] == board[9] == marker) \
            or (board[2] == board[5] == board[8] == marker) \
            or (board[3] == board[5] == board[7] == marker) \
            or (board[1] == board[5] == board[9] == marker):
        won = True
        print 'Player ' + marker + ' wins'

    return won

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    free = False
    if board[position] == ' ':
        free = True
    return free

def full_board_check(board):
    for x in board:
        if x == ' ':
            full = False
        else:
            full = True

    if full == True:
        print 'Its a Tie!'
    return full

def player_choice(board):
    pos = input('Input Position from (1-9): ')
    if  space_check(board, pos) == True:
        return pos
    else:
        print ('Position already taken')
        return player_choice(board)

#Replay
def replay():
    play = raw_input('Do you want to play again?: ')
    return play

#Begin Playing
def main_app():
    print ('Welcome To Tic Tac Toe')
    #Initalize Board
    test_board = [' ']*10

    #Display Board
    display_board(test_board)
    player1, player2 = player_input()

    goesFirst = choose_first();
    print goesFirst + ' goes first'

    while full_board_check(test_board) == False:
        #Place Marker
        if goesFirst == 'Player 1':
            print '\n<'+ goesFirst +'>'
            pos = player_choice(test_board)
            update_place_mark(pos, player1, test_board)
            goesFirst = 'Player 2'

            if check_winner(test_board, player1):
                break
        else:
            print '\n<' + goesFirst + '>'
            pos = player_choice(test_board)
            update_place_mark(pos, player2, test_board)
            goesFirst = 'Player 1'

            if check_winner(test_board, player2):
                break

    if replay() == 'Y':
        main_app()
    else:
        print 'Thanks for playing!'

#Launch Application
main_app()














