from server.simulator.game import Game
from server.simulator.data import Board
from server.common.functions import dotest

def simulation_test():
    dotest("ScoreTest1", test_1)
    dotest("ScoreTest2", test_2)
    dotest("ScoreTest3", test_3)
    dotest("ScoreTest4", test_4)
    dotest("ScoreTest5", test_5)
    dotest("ScoreTest6", test_6)


def test_1():
    # SCORE TEST 1
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


def test_2():
    # SCORE TEST 2
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


def test_3():
    # SCORE TEST 3
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


def test_4():
    # SCORE TEST 4
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


def test_5():
    # SCORE TEST 5
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


def test_6():
    # SCORE TEST 6
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

