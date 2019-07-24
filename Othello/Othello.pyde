from board import Board

WIDTH = 640
HEIGHT = 640
SIZE = 8
COLOR = green
BLACK = 0
WHITE = 255
DELAY_TIME = 10
delay_count = 0
player_turn = False
answer = ""

game_board = Board(WIDTH, HEIGHT, SIZE)

def setup():
    global answer
    size(WIDTH, HEIGHT)
    background(0, 153, 0)
    game_board.start_game()
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == '':
        print('[empty string]')
    else:
        print(answer) # Canceled dialog will print None
    print("Your turn")

def input(message):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def draw():
    global delay_count
    global player_turn
    global answer
    if not game_board.display(answer):
        # Take computer's turn
        if game_board.current_color == WHITE:
            if delay_count == DELAY_TIME:
                delay_count = 0
                player_turn = True
                game_board.comp_place_piece()
            elif delay_count == 0:
                print("Computer's turn.")
                delay_count += 1
            else:
                delay_count += 1
        # Checks of user has valid move
        else:
            if player_turn:
                print("Your turn.")
                game_board.user_place_piece()
                player_turn = False

def mouseClicked():
    if game_board.current_color == BLACK:
        game_board.place_piece(mouseX, mouseY)
