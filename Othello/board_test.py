from board import Board
from game_piece import GamePiece

# A test for the board class of Othello

BLACK = 0
WHITE = 255


def test___init__():
    """A test for constructor of the board class"""
    board = Board(640, 640, 4)
    assert (board.WIDTH == 640
            and board.HEIGHT == 640
            and board.SIZE == 4
            and board.SPACE_SIZE == 640 // 4
            and board.CLICK_RADIUS == (640//4)/2 - 10
            and board.hort_lines == []
            and board.vert_lines == []
            and board.game_pieces == []
            and board.piece_location == []
            and board.used_points == set()
            and board.current_color == BLACK
            and board.previous_no_moves is False
            and board.score is True)
    
    board = Board(640, 640, 8)
    assert (board.WIDTH == 640
            and board.HEIGHT == 640
            and board.SIZE == 8
            and board.SPACE_SIZE == 640 // 8
            and board.CLICK_RADIUS == (640//8)/2 - 10
            and board.hort_lines == []
            and board.vert_lines == []
            and board.game_pieces == []
            and board.piece_location == []
            and board.used_points == set()
            and board.current_color == BLACK
            and board.previous_no_moves is False
            and board.score is True)

def test_start_game():
    """A test for start_game()"""
    board = Board(640, 640, 8)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    board.start_game()
    exp_list = []
    for x in range(8):
        for y in range(8):
            exp_list.append(((board.SPACE_SIZE/2) + (board.SPACE_SIZE * x),
                             (board.SPACE_SIZE/2) + (board.SPACE_SIZE * y)))
    assert board.piece_location == exp_list
    exp_game_pieces = []
    for _i in range(8):
        current_list = []
        for _j in range(8):
            current_list.append(None)
        exp_game_pieces.append(current_list)
    exp_game_pieces[3][3] = white_piece
    exp_game_pieces[3][4] = black_piece
    exp_game_pieces[4][3] = black_piece
    exp_game_pieces[4][4] = white_piece
    for i in range(8):
        for j in range(8):
            if board.game_pieces[i][j] is None:
                assert exp_game_pieces[i][j] is None
            else:
                assert board.game_pieces[i][j].color == exp_game_pieces[i][j].color

def test_create_lines():
    """A test for create_lines()"""
    board = Board(640, 640, 8)
    exp_vert_lines = []
    exp_hort_lines = []
    for i in range(1, 8):
        exp_vert_lines.append((640//8)*i)
        exp_hort_lines.append((640//8)*i)
    board.create_lines()
    assert board.vert_lines == exp_vert_lines
    assert board.hort_lines == exp_hort_lines

    board = Board(640, 640, 4)
    exp_vert_lines = []
    exp_hort_lines = []
    for i in range(1, 4):
        exp_vert_lines.append((640//4)*i)
        exp_hort_lines.append((640//4)*i)
    board.create_lines()
    assert board.vert_lines == exp_vert_lines
    assert board.hort_lines == exp_hort_lines

def test_user_place_piece():
    """A test for user_place_piece()"""
    board = Board(640, 640, 8)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    board.start_game()

    board.game_pieces[3][3] = None
    board.game_pieces[3][4] = None
    board.game_pieces[4][3] = None
    board.game_pieces[4][4] = None
    board.user_place_piece()
    assert board.previous_no_moves is True and board.current_color == WHITE

    board.game_pieces[3][3] = white_piece
    board.game_pieces[3][4] = black_piece
    board.game_pieces[4][3] = black_piece
    board.game_pieces[4][4] = white_piece
    board.user_place_piece()
    assert board.previous_no_moves is False

def test_comp_place_piece():
    """A test for comp_place_piece()"""
    board = Board(640, 640, 8)
    black_piece = GamePiece(0, 0, BLACK, 0)
    white_piece = GamePiece(0, 0, WHITE, 0)
    board.start_game()

    board.game_pieces[3][3] = None
    board.game_pieces[3][4] = None
    board.game_pieces[4][3] = None
    board.game_pieces[4][4] = None
    board.comp_place_piece()
    assert board.previous_no_moves is True and board.current_color == BLACK

    board.game_pieces[3][3] = white_piece
    board.game_pieces[3][4] = black_piece
    board.game_pieces[4][3] = black_piece
    board.game_pieces[4][4] = white_piece
    num_pieces = len(board.used_points)
    board.comp_place_piece()
    assert board.previous_no_moves is False and len(board.used_points) == num_pieces + 1

def test_place_piece():
    """A test for place_piece()"""
    board = Board(640, 640, 4)
    board.start_game()
    board.place_piece(board.SPACE_SIZE/2, 0)
    assert len(board.used_points) == 4

def test_place_piece_helper():
    """A test for place_piece_helper()"""
    board = Board(640, 640, 8)
    board.start_game()
    board.place_piece_helper(0, 0, 0, 0)
    assert len(board.used_points) == 5 and board.current_color == WHITE
    board.place_piece_helper(1, 0, 1, 0)
    assert len(board.used_points) == 6 and board.current_color == BLACK

def test_check_point():
    """A test for check_point()"""
    board = Board(640, 640, 8)
    board.start_game()
    assert board.check_point(board.SPACE_SIZE/2, board.SPACE_SIZE/2) is not None
    assert board.check_point(0, 0) is None

def test_flip_piece():
    """A test for flip_pieces()"""
    board = Board(640, 640, 8)
    board.start_game()
    board.gm.flip_pieces = [(3, 3)]
    current_color = board.game_pieces[3][3].color
    board.flip_pieces()
    assert board.game_pieces[3][3].color != current_color
   
    board.gm.flip_pieces = [(3, 4)]
    current_color = board.game_pieces[3][4].color
    board.flip_pieces()
    assert board.game_pieces[3][4].color != current_color

def test_add_score():
    """A test for add_score()"""
    board = Board(640, 640, 8)
    board.add_score("test.txt", "User1", 5)
    board.add_score("test.txt", "User2", 10)
    board.add_score("test.txt", "User3", 6)
    board.add_score("test.txt", "User4", 11)
    open_file = open("test.txt", "r")
    file_lines = []
    for line in open_file:
        file_lines.append(line.strip())
    assert file_lines[0] == "User4 11"
    assert file_lines[1] == "User2 10"
    assert file_lines[2] == "User1 5"
    assert file_lines[3] == "User3 6"
