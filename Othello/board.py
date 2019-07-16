from game_piece import GamePiece
from game_manager import GameManager
from computer_ai import ComputerAi

# A board game for Othello

BLACK = 0
WHITE = 255


class Board:
    """A class for the Othello board"""

    def __init__(self, WIDTH, HEIGHT, SIZE):
        """Creates an instance of a board for Othello given the width, height,
        and size of the board.
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SIZE = SIZE
        self.SPACE_SIZE = WIDTH // SIZE
        self.CLICK_RADIUS = (self.SPACE_SIZE/2) - 10
        self.hort_lines = []
        self.vert_lines = []
        self.game_pieces = []
        self.piece_location = []
        self.used_points = set()
        self.gm = GameManager(SIZE)
        self.current_color = BLACK
        self.previous_no_moves = False
        self.score = True

    def start_game(self):
        """Displays the first four pieces of the game"""
        # Defines where game pieces can be placed
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                self.piece_location.append(((self.SPACE_SIZE/2) + (self.SPACE_SIZE * x),
                                            (self.SPACE_SIZE/2) + (self.SPACE_SIZE * y)))

        # Creates empty board in list form
        for _i in range(self.SIZE):
            current_list = []
            for _j in range(self.SIZE):
                current_list.append(None)
            self.game_pieces.append(current_list)

        # Creates (x,y) to place the first four pieces
        x_mid = self.WIDTH // 2
        y_mid = self.HEIGHT // 2
        mid_space = self.SPACE_SIZE / 2

        right_x = int(x_mid + mid_space)
        left_x = int(x_mid - mid_space)
        bottom_y = int(y_mid - mid_space)
        top_y = int(y_mid + mid_space)
        self.place_piece_helper(right_x//self.SPACE_SIZE, bottom_y//self.SPACE_SIZE,
                                right_x, bottom_y)
        self.place_piece_helper(right_x//self.SPACE_SIZE, top_y//self.SPACE_SIZE,
                                right_x, top_y)
        self.place_piece_helper(left_x//self.SPACE_SIZE, top_y//self.SPACE_SIZE,
                                left_x, top_y)
        self.place_piece_helper(left_x//self.SPACE_SIZE, bottom_y//self.SPACE_SIZE,
                                left_x, bottom_y)

    def create_lines(self):
        """Draws the game board lines according to the size of the game"""
        for i in range(1, self.SIZE):
            self.vert_lines.append((self.WIDTH//self.SIZE) * i)
            self.hort_lines.append((self.HEIGHT//self.SIZE) * i)

    def display(self, user_name):
        """Displays the game of the board"""
        # Displays game lines
        stroke(0, 0, 10)
        strokeWeight(3)
        self.create_lines()
        for x in self.vert_lines:
            line(x, 0, x, self.HEIGHT)
        for y in self.hort_lines:
            line(0, y, self.WIDTH, y)

        # Display pieces of the game
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.game_pieces[i][j] is not None:
                    self.game_pieces[i][j].display()

        # Displays end message if game ends
        black_count = self.gm.end_game(self.game_pieces, self.used_points)
        if self.gm.game_over is True:
            self.gm.display_winner()
            if self.score is True:
                self.add_score("scores.txt", user_name, black_count)
                self.score = False
            return True

    def user_place_piece(self):
        """Allows the user to place a piece on the board"""
        if self.gm.game_over is False:    
            valid_moves = self.gm.get_valid_moves(
                self.game_pieces, self.current_color)
            if len(valid_moves) == 0:
                if self.previous_no_moves is True:
                    self.gm.game_over = True
                else:
                    self.previous_no_moves = True
                print("No valid moves.")
                self.current_color = WHITE
            else:
                self.previous_no_moves = False

    def comp_place_piece(self):
        """Places a piece for the computer if there is a valid move"""
        if self.gm.game_over is False:
            valid_moves = self.gm.get_valid_moves(
                self.game_pieces, self.current_color)
            if len(valid_moves) != 0:
                computer = ComputerAi(valid_moves, self.SIZE)
                i, j = computer.find_best_move()
                x = (self.SPACE_SIZE/2) + (self.SPACE_SIZE * i)
                y = (self.SPACE_SIZE/2) + (self.SPACE_SIZE * j)
                self.place_piece(x, y)
                self.previous_no_moves = False
            else:
                if self.previous_no_moves is True:
                    self.gm.game_over = True
                else:
                    self.previous_no_moves = True
                print("No valid moves.")
                self.current_color = BLACK

    def place_piece(self, x, y):
        """Given x and y positions, places a new piece on the board if a 
        legal empty space
        """
        if self.check_point(x, y) is not None:
            clicked_point = self.check_point(x, y)
            x_position, y_position = clicked_point
            i = int(x_position // self.SPACE_SIZE)
            j = int(y_position // self.SPACE_SIZE)
            if (clicked_point not in self.used_points
                and self.gm.check_valid_move(i, j, self.game_pieces,
                                             self.current_color)):
                self.place_piece_helper(i, j, x_position, y_position)
                self.flip_pieces()

    def place_piece_helper(self, i, j, x, y):
        """Given an x,y positions and i, j positions that correspond to the list
        position, places a game piece
        """
        self.used_points.add((x, y))
        self.game_pieces[i][j] = GamePiece(x, y, self.current_color,
                                           self.SPACE_SIZE)
                                 
        if self.current_color == WHITE:
            self.current_color = BLACK
        else:
            self.current_color = WHITE

    def check_point(self, x, y):
        """Returns the coordinate of the piece location upon mouse click
        if it is a legal location to place a piece.
        """
        for coordinate in self.piece_location:
            if (abs(x - coordinate[0]) <= self.CLICK_RADIUS
                    and abs(y - coordinate[1]) <= self.CLICK_RADIUS):
                return coordinate

    def flip_pieces(self):
        """Flips the pieces of the valid move"""
        for x, y in self.gm.flip_pieces:
            if self.game_pieces[x][y].color == WHITE:
                self.game_pieces[x][y].color = BLACK
            else:
                self.game_pieces[x][y].color = WHITE
    
    def add_score(self, file_name, user_name, black_count):
        """Given the username and user's score, opens the scores file and
        adds the score to the top of the file if it's bigger than the highest
        score, otherwise adds the new score to the end of the file
        """
        try:
            open_file = open(file_name, "r+")
            score_data = []
            result = user_name + " " + str(black_count)
            for line in open_file:
                score_data.append(line)
            if len(score_data) == 0:
                open_file.write(result)
            else:
                first_line_words = score_data[0].split()
                prev_score = int(first_line_words[len(first_line_words) - 1])
                if black_count > prev_score:
                    open_file.seek(0)
                    result += "\n"
                    for line in score_data:
                        result += line
                    open_file.write(result)
                else:
                    result = "\n" + result
                    open_file.write(result)
                open_file.close()
        except:
            print(file_name, "does not exist")
