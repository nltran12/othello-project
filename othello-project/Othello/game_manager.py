# A game manager class for Othello

BLACK = 0
WHITE = 255
MSSG_SIZE = 320


class GameManager:
    """A Game Manager class for Othello"""

    def __init__(self, size):
        """Creates an instances of GameManager given the game grid"""
        self.SIZE = size
        self.winner = None
        self.win_score = 0
        self.lose_score = 0
        self.total_piece_count = size * size
        self.game_over = False
        self.flip_pieces = []

    def end_game(self, game_pieces, used_points):
        """Determines and displays the winner of the game"""
        current_piece_count = self.update_piece_count(used_points)
        if current_piece_count == self.total_piece_count:
            self.game_over = True
        if self.game_over is True:
            black_count, white_count = self.count_colors(game_pieces)
            if black_count > white_count:
                self.winner = "Black"
                self.win_score = black_count
                self.lose_score = white_count
            elif white_count > black_count:
                self.winner = "White"
                self.win_score = white_count
                self.lose_score = black_count
            else:
                self.win_score = black_count
                self.lose_score = white_count
            return black_count

    def display_winner(self):
        """Displays the end game message"""
        if self.winner is None:
            message = "TIE, {0} - {1}".format(self.win_score, self.lose_score)
        else:
            message = "{} Wins, {} - {}".format(self.winner, self.win_score,
                                                self.lose_score)
        self.display_mssg(message)

    def display_mssg(self, message):
        """Displays the end game message"""
        textSize(32)
        tw = textWidth(message)
        ta = textAscent()
        td = textDescent()

        stroke(0)
        strokeWeight(4)
        fill(WHITE)
        rectMode(CENTER)
        rect(MSSG_SIZE, MSSG_SIZE, tw + 20, ta + td + 20)

        fill(50)
        textAlign(CENTER, CENTER)
        text(message, MSSG_SIZE, MSSG_SIZE)

    def count_colors(self, game_pieces):
        """Returns number of black and white game pieces currently on the board"""
        black_count = 0
        white_count = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if game_pieces[i][j] is not None:
                    if game_pieces[i][j].color == BLACK:
                        black_count += 1
                    else:
                        white_count += 1
        return black_count, white_count

    def update_piece_count(self, used_points):
        """Return the number of pieces on the board"""
        return len(used_points)

    def check_valid_move(self, x, y, game_pieces, current_color):
        if current_color == WHITE:
            opposing_color = BLACK
        else:
            opposing_color = WHITE
        self.flip_pieces = []
        surrounding_positions = [(1, 0), (0, 1), (-1,1), (1,-1), (1,1), 
                                 (-1, -1), (-1, 0), (0, -1)]
        # Checks if space is next to an opposing piece
        for x_direction, y_direction in surrounding_positions:
            current_x = int(x + x_direction)
            current_y = int(y + y_direction)
            if self.on_board(current_x, current_y):
                piece = game_pieces[current_x][current_y]

                # Continues to check if the next piece is an opposiing piece
                while piece is not None and piece.color == opposing_color:
                    current_x = int(current_x + x_direction)
                    current_y = int(current_y + y_direction)
                    if not self.on_board(current_x, current_y):
                        break
                    piece = game_pieces[current_x][current_y]

                # Checks if the opposing pieces are next to the current piece
                if piece is not None and piece.color == current_color:
                    while current_x != x or current_y != y:
                        current_x = int(current_x - x_direction)
                        current_y = int(current_y - y_direction)
                        if current_x != x or current_y != y:
                            self.flip_pieces.append((current_x, current_y))

        if len(self.flip_pieces) == 0:
            return False
        return True

    def get_valid_moves(self, game_pieces, current_color):
        """Returns a list of valid moves"""
        valid_moves = []
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if (game_pieces[i][j] is None
                    and self.check_valid_move(i, j, game_pieces, current_color)):
                    valid_moves.append((i, j))
        return valid_moves

    def on_board(self, x, y):
        """Checks if the given x and y coordinates are within 
        the size of the board
        """
        return x >= 0 and x < self.SIZE and y >= 0 and y < self.SIZE
