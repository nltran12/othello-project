from game_manager import GameManager

# A class of the computer AI for a game of othello


class ComputerAi:
    """A computer moveset AI for othello"""

    def __init__(self, valid_moves, size):
        """Creates an instance of the computer AI given the valid moves 
        and board size
        """
        self.valid_moves = valid_moves
        self.size = size

    def find_best_move(self):
        """Returns the best move for the computer
        None -> tuple(int, int)
        """
        move = None
        if self.find_corner_piece() is not None:
            move = self.find_corner_piece()
        elif self.find_edge_piece() is not None:
            move = self.find_edge_piece()
        else:
            if len(self.valid_moves) > 0:
                move = self.valid_moves[0]
        return move

    def find_corner_piece(self):
        """Returns the coordinates of a valid corner location move, 
        otherwise returns None
        """
        corner_locations = [(0, 0), (0, self.size - 1), (self.size - 1, 0),
                            (self.size - 1, self.size - 1)]
        for location in corner_locations:
            if self.valid_moves.count(location) > 0:
                return location

    def find_edge_piece(self):
        """Return the coordinates of a valid edge location move,
        otherwise returns None
        """
        edge_locations = []
        for i in range(0, self.size):
            edge_locations.append((0, i))
            edge_locations.append((i, 0))
            edge_locations.append((self.size - 1, i))
            edge_locations.append((i, self.size - 1))
        for location in edge_locations:
            if self.valid_moves.count(location) > 0:
                return location
