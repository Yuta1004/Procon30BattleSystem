from server.simulator.game import Game
from server.simulator.board import Board, _generate_line_symmetry_half_A,\
    _generate_line_symmetry_half_B, _generate_line_symmetry_quarter, _generate_point_symmetry
from server.simulator.agent import Agent
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
    dotest("GenerateBoardTest5", generate_board_test_5)
    dotest("GenerateBoardTest6", generate_board_test_6)
    dotest("GenerateBoardTest7", generate_board_test_7)

    dotest("FlowTest1", flow_test_1)
    dotest("FlowTest2", flow_test_2)


# Score Calculate Test
def score_test_1():
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
    board = Board(width, height, points, tiled)
    game = Game(board, [])
    true_score = {
        1: {
            "tilePoint": 2,
            "areaPoint": 4
        },
        2: {
            "tilePoint": 4,
            "areaPoint": 0
        }
    }
    assert(game.cal_score([1, 2]) == true_score)


def score_test_2():
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
    board = Board(width, height, points, tiled)
    game = Game(board, [])
    true_score = {
        1: {
            "tilePoint": 3,
            "areaPoint": 2
        },
        2: {
            "tilePoint": 3,
            "areaPoint": 2
        }
    }
    assert(game.cal_score([1, 2]) == true_score)


def score_test_3():
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
    board = Board(width, height, points, tiled)
    game = Game(board, [])
    true_score = {
        1: {
            "tilePoint": 22,
            "areaPoint": 10
        },
        2: {
            "tilePoint": 2,
            "areaPoint": 4
        }
    }
    assert(game.cal_score([1, 2]) == true_score)


def score_test_4():
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
    board = Board(width, height, points, tiled)
    game = Game(board, [])
    true_score = {
        1: {
            "tilePoint": 10,
            "areaPoint": 10
        },
        2: {
            "tilePoint": 2,
            "areaPoint": 4
        }
    }
    assert(game.cal_score([1, 2]) == true_score)


def score_test_5():
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
    board = Board(width, height, points, tiled)
    game = Game(board, [])
    true_score = {
        1: {
            "tilePoint": 15,
            "areaPoint": 4
        }
    }
    assert (game.cal_score([1]) == true_score), "Test Failed"


def score_test_6():
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
    board = Board(width, height, points, tiled)
    game = Game(board, [])
    true_score = {
        1: {
            "tilePoint": 32,
            "areaPoint": 22
        }
    }
    assert(game.cal_score([1]) == true_score)


# Board Generate Test(Line Sysmmetry)
def generate_board_test_1():
    points = _generate_line_symmetry_half_A(10, 6, 0, 16)
    assert _is_line_symmetry_half_y(points)


def generate_board_test_2():
    points = _generate_line_symmetry_half_A(5, 9, 0, 16)
    assert _is_line_symmetry_half_y(points)


def generate_board_test_3():
    points = _generate_line_symmetry_half_B(10, 9, 0, 16)
    assert _is_line_symmetry_half_x(points)


def generate_board_test_4():
    points = _generate_line_symmetry_half_B(3, 9, 0, 16)
    assert _is_line_symmetry_half_x(points)


def generate_board_test_5():
    points = _generate_line_symmetry_quarter(10, 9, 0, 16)
    assert _is_line_symmetry_half_x(points)
    assert _is_line_symmetry_half_y(points)


def generate_board_test_6():
    points = _generate_line_symmetry_quarter(5, 12, 0, 16)
    assert _is_line_symmetry_half_x(points)
    assert _is_line_symmetry_half_y(points)


# Board Generate Test(Pont Symmetry)
def generate_board_test_7():
    points = _generate_point_symmetry(10, 7, 0, 9)
    assert _is_point_symmetry(points)


def generate_board_test_8():
    points = _generate_point_symmetry(9, 8, 0, 9)
    assert _is_point_symmetry(points)


# Flow Test
def flow_test_1():
    width = 5
    height = 5
    points = [
        [2, 1, 0, 1, 2],
        [4, 5, 3, 5, 4],
        [1, 1, 2, 1, 1],
        [4, 5, 3, 5, 4],
        [2, 1, 0, 1, 2]
    ]
    tiled = [
        [0, 1, 0, 2, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 2, 0, 1, 0]
    ]
    agents = [
        Agent(1, 1, 1, 0),
        Agent(1, 2, 3, 4),
        Agent(2, 3, 3, 0),
        Agent(2, 4, 1, 4)
    ]
    board = Board(width, height, points, tiled)
    simulator = Game(board, agents)
    simulator.set_action(1, 1, 0, 1)
    simulator.set_action(1, 2, -1, 0)
    simulator.set_action(2, 3, 1, 0)
    simulator.set_action(2, 4, 0, -1)
    simulator.step()

    true_score = {
        1: {
            "tilePoint": 7,
            "areaPoint": 0
        },
        2: {
            "tilePoint": 9,
            "areaPoint": 0
        }
    }
    assert(simulator.cal_score([1, 2]) == true_score)
    assert(simulator.turn == 1)


def flow_test_2():
    width = 7
    height = 3
    points = [
        [1, 4, -2, 5, -2, 4, 1],
        [8, 9, 1, 0, 1, 9, 8],
        [0, 4, 6, 3, 6, 4, 0],
    ]
    tiled = [
        [0, 0, 1, 0, 2, 0, 0],
        [0, 0, 1, 0, 2, 0, 0],
        [0, 0, 1, 0, 2, 0, 0]
    ]
    agents = [
        Agent(1, 1, 2, 0),
        Agent(1, 2, 2, 1),
        Agent(1, 3, 2, 2),
        Agent(2, 4, 4, 0),
        Agent(2, 5, 4, 1),
        Agent(2, 6, 4, 2),
    ]
    board = Board(width, height, points, tiled)
    simulator = Game(board, agents)

    # 1
    simulator.set_action(1, 1, 1, 0)
    simulator.set_action(1, 2, 1, 0)
    simulator.set_action(1, 3, -1, 0)
    simulator.set_action(2, 4, 1, 0)
    simulator.set_action(2, 5, -1, 0)
    simulator.set_action(2, 6, -1, 0)
    simulator.step()

    true_score = {
        1: {
            "tilePoint": 14,
            "areaPoint": 0
        },
        2: {
            "tilePoint": 12,
            "areaPoint": 0
        }
    }
    assert(simulator.cal_score([1, 2]) == true_score)
    assert(simulator.turn == 1)


# For Test Function
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


def _is_point_symmetry(target):
    width = len(target[0])
    height = len(target)
    result = True
    for y in range(height):
        for x in range(width):
            result &= (target[height - y - 1][width - x - 1] == target[y][x])
    return result
