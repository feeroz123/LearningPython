# Tic Tac Toe game for two players
from IPython.display import clear_output
import random

board = [' ']*10
pattern_x = []
pattern_o = []
valid_locations = [1,2,3,4,5,6,7,8,9]
success_pattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]



def draw_board():
    clear_output()
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
    result = random.randint(0,1)

    print('****************************')
    if result == 0:
        print('* Player 1 wins the toss ! *')
    else:
        print('* Player 2 wins the toss ! *')
    print('****************************')

    return result

def mark_board(input_location,marker):
    board[input_location] = marker
    draw_board()

def game_action(player, marker):

    print('Valid locations: ', valid_locations)
    player_input_location = int(input(f'{player} : Enter your mark location \n(press 0 to exit game) ----> '))

    # Check if 0 is entered then Exit the game
    if player_input_location == 0:
        print('Game Exited')
        exit(0)
    # Validating input location
    elif player_input_location not in valid_locations:
        print('Invalid Input ! Your turn is cancelled.')
        return
    else:
        # Update the board for the player
        print('Player Input Location = ', player_input_location)
        mark_board(player_input_location, marker)
        valid_locations.remove(player_input_location)
        check_winner(player)

def check_winner(player):

    for counter, value in enumerate(board):
        if value == 'x':
            pattern_x.append(counter)
        elif value == 'o':
            pattern_o.append(counter)

    if pattern_x in success_pattern:
        print(f'{player} WINS !!!')
        print(pattern_x)
        print("Game Over.")
        exit(0)

    elif pattern_o in success_pattern:
        print(f'{player} WINS !!!')
        print(pattern_o)
        print("Game Over.")
        exit(0)



print('\nWelcome to the TIC-TAC-TOE game !')
print('=========================================')

# Choose player markers
player1_mark, player2_mark = player_marker()
print('\nPlayer 1 marker is : ' + player1_mark + ' , and Player 2 marker is: ' + player2_mark)

# Perform toss
print('\n      Lets do the toss !\n')
if toss():
    winner = 'Player 1'
    winner_marker = player1_mark
    loser = 'Player 2'
    loser_marker = player2_mark
else:
    winner = 'Player 2'
    winner_marker = player2_mark
    loser = 'Player 1'
    loser_marker = player1_mark


# Begin the game
initiate_trigger = input("\nLet's begin the game now!! Good luck to both players! \n\nEnter Y to continue .....")

# Check for the game to continue
if not initiate_trigger.lower() == 'y':
    print("Game is exited.")
    exit(0)
else:
    draw_board()


while len(valid_locations) > 0:
        game_action(winner, winner_marker)
        game_action(loser, loser_marker)

print("No Winner. Game is Over")