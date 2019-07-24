from game_manager import GameManager
from game_piece import GamePiece

# A test for game manager of Othello

BLACK = 0
WHITE = 255


def test___init__():
    """A test for the constructor of the GameManager"""
    gm = GameManager(8)
    assert (gm.SIZE == 8 
            and gm.winner is None
            and gm.win_score == 0
            and gm.lose_score == 0
            and gm.total_piece_count == 64
            and gm.game_over is False
            and len(gm.flip_pieces) == 0)
    gm = GameManager(4)
    assert (gm.SIZE == 4
            and gm.winner is None
            and gm.win_score == 0
            and gm.lose_score == 0
            and gm.total_piece_count == 16
            and gm.game_over is False
            and len(gm.flip_pieces) == 0)
    gm = GameManager(0)
    assert (gm.SIZE == 0
            and gm.winner is None
            and gm.win_score == 0
            and gm.lose_score == 0
            and gm.total_piece_count == 0
            and gm.game_over is False
            and len(gm.flip_pieces) == 0)

def test_end_game():
    """A test for end_game()"""
    gm = GameManager(4)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    game_pieces = []
    for _i in range(4):
        piece_list = []
        for _j in range(4):
            piece_list.append(None)
        game_pieces.append(piece_list)

    game_pieces[0][0] = black_piece
    used_pieces = [1, 2, 3, 4]
    assert (gm.end_game(game_pieces, used_pieces) is None
            and gm.game_over is False)

    used_pieces += [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16]
    assert (gm.end_game(game_pieces, used_pieces) is 1
            and gm.game_over is True
            and gm.win_score == 1
            and gm.lose_score == 0
            and gm.winner == "Black")

    game_pieces[1][1] = white_piece
    assert (gm.end_game(game_pieces, used_pieces) is 1
            and gm.game_over is True
            and gm.win_score == 1
            and gm.lose_score == 1)

    game_pieces[2][2] = black_piece
    assert (gm.end_game(game_pieces, used_pieces) is 2
            and gm.game_over is True
            and gm.win_score == 2
            and gm.lose_score == 1
            and gm.winner == "Black")

    game_pieces[3][3] = white_piece
    game_pieces[0][2] = white_piece
    assert (gm.end_game(game_pieces, used_pieces) is 2
            and gm.game_over is True
            and gm.win_score == 3
            and gm.lose_score == 2
            and gm.winner == "White")

def test_count_colors():
    """A test for count_colors()"""
    gm = GameManager(8)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    game_pieces = []
    for _i in range(8):
        piece_list = []
        for _j in range(8):
            piece_list.append(None)
        game_pieces.append(piece_list)

    game_pieces[0][0] = black_piece
    black_count, white_count = gm.count_colors(game_pieces)
    assert black_count == 1 and white_count == 0

    game_pieces[1][1] = white_piece
    black_count, white_count = gm.count_colors(game_pieces)
    assert black_count == 1 and white_count == 1

    game_pieces[0][1] = black_piece
    game_pieces[1][2] = white_piece
    game_pieces[0][2] = black_piece
    black_count, white_count = gm.count_colors(game_pieces)
    assert black_count == 3 and white_count == 2

    game_pieces[0][0] = None
    black_count, white_count = gm.count_colors(game_pieces)
    assert black_count == 2 and white_count == 2

def test_update_piece_count():
    """A test for update_piece_count()"""
    gm = GameManager(8)
    
    used_points = []
    assert gm.update_piece_count(used_points) == 0

    used_points.append(1)
    assert gm.update_piece_count(used_points) == 1

    used_points += [2, 3]
    assert gm.update_piece_count(used_points) == 3

def test_check_valid_move():
    """A test for check_valid_move()"""
    gm = GameManager(4)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    game_pieces = []
    for _i in range(4):
        piece_list = []
        for _j in range(4):
            piece_list.append(None)
        game_pieces.append(piece_list)
    
    # game set up
    game_pieces[1][1] = white_piece
    game_pieces[1][2] = black_piece
    game_pieces[2][1] = black_piece
    game_pieces[2][2] = white_piece
    assert gm.check_valid_move(0, 1, game_pieces, BLACK) is True
    exp_flip_pieces = [(1, 1)]
    assert gm.flip_pieces == exp_flip_pieces
    assert gm.check_valid_move(0, 1, game_pieces, WHITE) is False

    game_pieces[0][0] = black_piece
    game_pieces[2][2] = white_piece
    assert gm.check_valid_move(3, 3, game_pieces, BLACK) is True
    exp_flip_pieces = [(1, 1), (2, 2)]
    assert gm.flip_pieces == exp_flip_pieces
    assert gm.check_valid_move(3, 3, game_pieces, WHITE) is False

    game_pieces[0][3] = white_piece
    assert gm.check_valid_move(3, 0, game_pieces, WHITE) is True
    exp_flip_pieces = [(1, 2), (2, 1)]
    assert gm.flip_pieces == exp_flip_pieces

def test_get_valid_moves():
    """A test for get_valid_moves()"""
    gm = GameManager(4)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    game_pieces = []
    for _i in range(4):
        piece_list = []
        for _j in range(4):
            piece_list.append(None)
        game_pieces.append(piece_list)
    
    # first 4 pieces game set up
    game_pieces[1][1] = white_piece
    game_pieces[1][2] = black_piece
    game_pieces[2][1] = black_piece
    game_pieces[2][2] = white_piece

    exp_list = [(1, 0), (0, 1), (2, 3), (3, 2)]
    valid_moves = gm.get_valid_moves(game_pieces, BLACK)
    for move in valid_moves:
        assert exp_list.count(move) == 1
    
    exp_list = [(2, 0), (1, 3), (0, 2), (3, 1)]
    valid_moves = gm.get_valid_moves(game_pieces, WHITE)
    for move in valid_moves:
        assert exp_list.count(move) == 1

def test_on_board():
    """A test for on_board()"""
    gm = GameManager(4)
    assert gm.on_board(4, 4) is False
    assert gm.on_board(0, 0) is True
    assert gm.on_board(4, 0) is False
    assert gm.on_board(0, 4) is False
    assert gm.on_board(3, 3) is True

    gm = GameManager(8)
    assert gm.on_board(8, 8) is False
    assert gm.on_board(0, 0) is True
    assert gm.on_board(8, 0) is False
    assert gm.on_board(0, 8) is False
    assert gm.on_board(4, 7) is True
