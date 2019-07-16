# A game piece for Othello

SIZE_FROM_BORDER = 10


class GamePiece:
    """A class for a game piece in Othello"""

    def __init__(self, x, y, color, SIZE):
        """Creates an instance of the Othello game piece given the x and y coordinate,
        color, and size
        """
        self.x = x
        self.y = y
        self.SIZE = SIZE - SIZE_FROM_BORDER
        self.color = color

    def display(self):
        """Displays the game piece"""
        fill(self.color)
        stroke(0)
        strokeWeight(2)
        ellipse(self.x, self.y, (self.SIZE), (self.SIZE))
