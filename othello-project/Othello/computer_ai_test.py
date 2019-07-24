from computer_ai import ComputerAi

# A test for the computer ai class of Othello

BLACK = 0
WHITE = 255

def test___init__():
    """A test for the constructor of the computer ai class of Othello"""
    valid_moves = [(5,5)]
    size = 8
    comp = ComputerAi(valid_moves, size)
    assert comp.valid_moves == valid_moves and comp.size == size
    valid_moves = []
    size = 8
    comp = ComputerAi(valid_moves, size)
    assert comp.valid_moves == valid_moves and comp.size == size

def test_find_best_move():
    """A test for find_best_move()"""
    valid_moves = [(5,5)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_best_move() == (5,5)

    valid_moves = []
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_best_move() is None

    valid_moves = [(5,5), (0,0)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_best_move() == (0,0)

    valid_moves = [(5,5), (0,4), (0,0)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_best_move() == (0,0)

    valid_moves = [(5,5), (0,4)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_best_move() == (0,4)

def test_find_corner_piece():
    """A test for find_corner_piece()"""
    valid_moves = [(5,5)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_corner_piece() is None

    valid_moves = [(5,5), (0,0)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_corner_piece() == (0,0)

    valid_moves = [(5,5), (0,4), (0,0)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_corner_piece() == (0,0)

    valid_moves = []
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_corner_piece() is None

def test_find_edge_piece():
    """A test for find_edge_piece()"""
    valid_moves = [(5,5)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_edge_piece() is None

    valid_moves = [(5,5), (2,2), (0,4)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_edge_piece() == (0,4)

    valid_moves = [(5,5), (4,4), (4,0)]
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_edge_piece() == (4,0)

    valid_moves = []
    comp = ComputerAi(valid_moves, 8)
    assert comp.find_edge_piece() is None