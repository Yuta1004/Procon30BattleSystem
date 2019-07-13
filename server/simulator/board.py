from random import randint
from server.simulator.values import *
from server.common.functions import gen_2d_list, transpositon_2d_list


class Board:
    def __init__(self, turn, width, height, points, tiled):
        self.turn = turn
        self.width = width
        self.height = height
        self.points = points
        self.tiled = tiled


def generate_board(width, height, point_upper, point_lower, generate_type=LINE_SYMMETRY_HALF):
    pass


def _generate_line_symmetry_half_A(width, height, point_upper, point_lower):
    board = gen_2d_list(height, width)

    # 基準となる点配置を作成
    base_width = (width + 1) / 2
    base_height = (height + 1) / 2
    for y in range(base_height):
        for x in range(base_width):
            board[y][x] = randint(point_lower, point_upper)

    # 対象となるように点を配置していく
    for y in range(base_height - 1, height):
        for x in range(base_width - 1, width):
            board[y][x] = board[y][width - x - 1]

    return board


def _generate_line_symmetry_half_B(width, height, point_upper, point_lower):
    return transpositon_2d_list(
        _generate_line_symmetry_half_A(width, height, point_upper, point_lower)
    )
