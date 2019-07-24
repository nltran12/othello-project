from game_piece import GamePiece

# A test for game piece of Othello

BLACK = 0
WHITE = 255


def test___init__():
    """Tests the init method"""
    gp = GamePiece(100, 100, BLACK, 160)
    assert gp.x == 100 and gp.y == 100 and gp.color == BLACK and gp.SIZE == 150
    gp = GamePiece(640, 250, WHITE, 100)
    assert gp.x == 640 and gp.y == 250 and gp.color == WHITE and gp.SIZE == 90