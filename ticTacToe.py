# Tic Tac Toe game for two players

import os
import random

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def draw_board():
    #board[location] = mark
    os.system('cls||clear')

    print('\n-------------------')
    print(f'|  {board[7]}  |  {board[8]}  |  {board[9]}  |')
    print('-------------------')
    print(f'|  {board[4]}  |  {board[5]}  |  {board[6]}  |')
    print('-------------------')
    print(f'|  {board[1]}  |  {board[2]}  |  {board[3]}  |')
    print('-------------------\n')

def player_marker():
    markers = ['x','o']
    player1_marker = ''
    while player1_marker.lower() not in markers:
        player1_marker = (input('Player 1 - Choose your marker, X or O : ')).upper()

    if player1_marker.lower() == 'x':
        player2_marker = 'O'
    else:
        player2_marker = 'X'

    return player1_marker, player2_marker

def toss():
    result = (random.randrange(1,100))%2 == 0

    print('****************************')
    if result:
        print('* Player 1 wins the toss ! *')
    else:
        print('* Player 2 wins the toss ! *')
    print('****************************')

    return result

def mark_board(input_location,marker):
    board[input_location] = marker
    draw_board()

def check_winner(player, marker):
    pass





print('\nWelcome to the TIC-TAC-TOE game !')
print('=========================================')

# Choose player markers
player1_mark, player2_mark = player_marker()
print('Player 1 marker is : ' + player1_mark + ' , and Player 2 marker is: ' + player2_mark)

# Perform toss
print('\n Lets do the toss !')
if toss():
    winner = 'Player 1'
    marker1 = player1_mark
    loser = 'Player 2'
    marker2 = player2_mark
else:
    winner = 'Player 2'
    marker1 = player2_mark
    loser = 'Player 1'
    marker2 = player1_mark




# Begin the game
initiate_trigger = input("\nLet's begin the game now!! Good luck to both players! \n Press Y to continue .....")

if not initiate_trigger.lower() == 'y':
    print("Game is exited.")
    exit(0)
else:
    draw_board()


valid_locations=['',1,2,3,4,5,6,7,8,9]

while len(valid_locations) > 1:

    # Winner player flow
    print('Available locations: ', valid_locations[1:])
    player_input_location = int(input(f'{winner} : Enter your mark location (press 0 to exit game) --> '))

    if player_input_location == 0:
        exit(0)
    elif player_input_location not in valid_locations:
        print('Invalid Input !')
        continue
    # Update the board for Winner player
    mark_board(player_input_location, marker1)
    valid_locations.remove(player_input_location)

    # Loser player flow
    print('Available locations: ', valid_locations[1:])
    player_input_location = int(input(f'{loser} : Enter your mark location (press 0 to exit game) --> '))

    if player_input_location == 0:
        exit(0)
    elif player_input_location not in valid_locations:
        print('Invalid Input !')
        continue

    # Update the board for Loser player
    mark_board(player_input_location, marker2)
    valid_locations.remove(player_input_location)

