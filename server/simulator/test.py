from server.simulator.game import Game
from server.simulator.board import Board, _generate_line_symmetry_half_A, _generate_line_symmetry_half_B
from server.common.functions import dotest, transpositon_2d_list

def simulation_test():
    dotest("ScoreTest1", score_test_1)
    dotest("ScoreTest2", score_test_2)
    dotest("ScoreTest3", score_test_3)
    dotest("ScoreTest4", score_test_4)
    dotest("ScoreTest5", score_test_5)
    dotest("ScoreTest6", score_test_6)

    dotest("GenerateBoardTest1", generate_board_test_1)
    dotest("GenerateBoardTest2", generate_board_test_2)
    dotest("GenerateBoardTest3", generate_board_test_3)
    dotest("GenerateBoardTest4", generate_board_test_4)


# Score Calculate Test
def score_test_1():
    turn = 10
    width = 8
    height = 5
    points = [
        [1, 0, 2, 1, 1, 2, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 3, -1, 2, 2, -1, 3, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 2, 1, 1, 2, 0, 1]
    ]
    tiled = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 2, 2, 1, 0 ,0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    board = Board(turn, width, height, points, tiled)
    game = Game("test1", board, [])
    assert (game.cal_score([1, 2]) == {1: 6, 2: 4}), "Test Failed"


def score_test_2():
    turn = 10
    width = 8
    height = 5
    points = [
        [1, 0, 2, 1, 1, 2, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 3, -1, 2, 2, -1, 3, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 2, 1, 1, 2, 0, 1]
    ]
    tiled = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 1, 2, 1, 2, 0 ,0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    board = Board(turn, width, height, points, tiled)
    game = Game("test1", board, [])
    assert (game.cal_score([1, 2]) == {1: 5, 2: 5}), "Test Failed"


def score_test_3():
    turn = 10
    width = 8
    height = 5
    points = [
        [1, 0, 2, 1, 1, 2, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 3, -1, 2, 2, -1, 3, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 2, 1, 1, 2, 0, 1]
    ]
    tiled = [
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 2, 2, 2, 2, 1, 0],
        [0, 1, 2, 0, 0, 2, 1 ,0],
        [0, 1, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0]
    ]
    board = Board(turn, width, height, points, tiled)
    game = Game("test1", board, [])
    assert (game.cal_score([1, 2]) == {1: 32, 2: 6}), "Test Failed"


def score_test_4():
    turn = 10
    width = 8
    height = 5
    points = [
        [1, 0, 2, 1, 1, 2, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 3, -1, 2, 2, -1, 3, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 2, 1, 1, 2, 0, 1]
    ]
    tiled = [
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 2, 2, 1, 0, 0],
        [0, 1, 2, 0, 0, 2, 1 ,0],
        [0, 0, 1, 2, 2, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0]
    ]
    board = Board(turn, width, height, points, tiled)
    game = Game("test1", board, [])
    assert (game.cal_score([1, 2]) == {1: 20, 2: 6}), "Test Failed"


def score_test_5():
    turn = 10
    width = 5
    height = 5
    points = [
        [-2, 0, 1, 0, -2],
        [1, 0, -2, 0, 1],
        [2, 2, 3, 2, 2],
        [2, 2, 3, 2, 2],
        [1, 0, -2, 0, 1]
    ]
    tiled = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    board = Board(turn, width, height, points, tiled)
    game = Game("test1", board, [])
    assert (game.cal_score([1]) == {1: 19}), "Test Failed"


def score_test_6():
    turn = 10
    width = 7
    height = 7
    points = [
        [0, 1, 2, 0, 2, 1, 0],
        [2, -2, 0, 1, 0, -2, 2],
        [2, 1, 0, -2, 0, 1, 2],
        [1, 2, 2, 3, 2, 2, 1],
        [1, 2, 2, 3, 2, 2, 1],
        [2, 1, 0, -2, 0, 1, 2],
        [2, -2, 0, 1, 0, -2, 2]
    ]
    tiled = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    board = Board(turn, width, height, points, tiled)
    game = Game("test1", board, [])
    assert (game.cal_score([1]) == {1: 54}), "Test Failed"


# Board Generate Test
def generate_board_test_1():
    points = _generate_line_symmetry_half_A(10, 6, 0, 16)
    assert _is_line_symmetry_half_y(points), "Test Failed"


def generate_board_test_2():
    points = _generate_line_symmetry_half_A(5, 9, 0, 16)
    assert _is_line_symmetry_half_y(points), "Test Failed"


def generate_board_test_3():
    points = _generate_line_symmetry_half_B(10, 9, 0, 16)
    assert _is_line_symmetry_half_x(points), "Test Failed"


def generate_board_test_4():
    points = _generate_line_symmetry_half_B(3, 9, 0, 16)
    assert _is_line_symmetry_half_x(points), "Test Failed"


def _is_line_symmetry_half_y(target):
    width = len(target[0])
    height = len(target)
    result = True
    for y in range(height):
        for x in range(width):
            result &= (target[y][x] == target[y][width - x - 1])
    return result


def _is_line_symmetry_half_x(target):
    return _is_line_symmetry_half_y(transpositon_2d_list(target))
