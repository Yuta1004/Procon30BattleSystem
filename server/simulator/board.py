from random import randint
from copy import deepcopy
from server.simulator.values import *
from server.common.functions import gen_2d_list, transpositon_2d_list


# Public
class Board:
    def __init__(self, turn, width, height, points, tiled):
        self.turn = turn
        self.width = width
        self.height = height
        self.points = points
        self.tiled = tiled


def generate_board(turn, width, height, point_upper, point_lower,\
                   player_num, generate_type=LINE_SYMMETRY_HALF):
    """
    指定された条件で盤面を生成し、そのデータを返す

    Params
    ----------
    turn : int
        ターン数
    width : int
        生成する盤面のサイズ(幅)
    height : int
        生成する盤面のサイズ(高さ)
    point_lower : int
        配置する得点の下限
    point_upper : int
        配置する得点の上限
    player_num : int
        配置するプレイヤーの数
    generate_type : int
        生成する盤面のタイプ、value.pyにある定数で指定すること

    Return
    ----------
    Board
        盤面情報
    """

    points = None
    tiled = None

    if generate_type == LINE_SYMMETRY_HALF:
        if randint(0, 1) == 0:
            points = _generate_line_symmetry_half_A(width, height, point_lower, point_upper)
            tiled = _put_player_line_symmetry_hq_A(width, height, player_num)
        else:
            points = _generate_line_symmetry_half_B(width, height, point_lower, point_upper)
            tiled = _put_player_line_symmetry_half_B(width, height, player_num)

    if generate_type == LINE_SYMMETRY_QUOTER:
        points = _generate_line_symmetry_quarter(width, height, point_lower, point_upper)
        tiled = _put_player_line_symmetry_hq_A(width, height, player_num)

    if generate_type == POINT_SYMMETRY_HALF:
        points = _generate_point_symmetry(width, height, point_lower, point_upper)
        tiled = _put_player_line_symmetry_hq_A(width, height)

    return Board(turn, width, height, points, tiled)


# Private
def _generate_line_symmetry_half_A(width, height, point_lower, point_upper):
    points = gen_2d_list(height, width)

    # 基準となる点配置を作成
    base_width = int((width + 1) / 2)
    for y in range(height):
        for x in range(base_width):
            points[y][x] = randint(point_lower, point_upper)

    # 対象となるように点を配置していく
    start_idx = base_width - (1 if len(points[0]) % 2 == 1 else 0)
    for y in range(height):
        points[y][start_idx:] = points[y][:base_width][::-1]

    return deepcopy(points)


def _put_player_line_symmetry_hq_A(width, height, player_num):
    tiled = gen_2d_list(height, width)
    base_width = int((width + 1) / 2)

    # 基準プレイヤー配置　
    for cnt in range(player_num):
        x = randint(0, base_width - 1)
        y = randint(0, height - 1)
        player = int(player_num % 2 == 0 and cnt % 2 == 0) + 1
        while (tiled[y][x] != 0) and (tiled[y][x] == player):
            x = randint(0, base_width - 1)
            y = randint(0, height - 1)
        tiled[y][x] = player

    # 線対称に配置する
    for y in range(height):
        for x in range(base_width):
            tiled[y][width - x - 1] = tiled[y][x]
            if (tiled[y][width - x - 1] == 1) and (player_num % 2 == 1):
                tiled[y][width - x - 1] = 2

    return deepcopy(tiled)


def _generate_line_symmetry_half_B(width, height, point_lower, point_upper):
    return transpositon_2d_list(
        _generate_line_symmetry_half_A(width, height, point_lower, point_upper)
    )


def _put_player_line_symmetry_half_B(width, height, player_num):
    return transpositon_2d_list(
        _put_player_line_symmetry_hq_A(width, height, player_num)
    )


def _generate_line_symmetry_quarter(width, height, point_lower, point_upper):
    points = gen_2d_list(height, width)

    # 基準となる点を設定する
    base_width = int((width + 1) / 2)
    base_height = int((height + 1) / 2)
    for y in range(base_height):
        for x in range(base_width):
            points[y][x] = randint(point_lower, point_upper)

    # 対称となるように点を配置していく
    start_idx_x = base_width - (1 if len(points[0]) % 2 == 1 else 0)
    start_idx_y = base_height - (1 if len(points) % 2 == 1 else 0)
    for y in range(height):
        points[y][start_idx_x:] = points[y][:base_width][::-1]
    for x in range(width):
        for y in range(height):
            points[height - y - 1][x] = points[y][x]

    return deepcopy(points)


def _generate_point_symmetry(width, height, point_lower, point_upper):
    points = gen_2d_list(height, width)

    # 基準となる点を設定する
    base_width = int((width + 1) / 2)
    for y in range(height):
        for x in range(base_width):
            points[y][x] = randint(point_lower, point_upper)

    # 点対称に得点を配置していく
    for x in range(width):
        for y in range(height):
            points[height - y - 1][width - x - 1] = points[y][x]

    return deepcopy(points)


def _put_player_point_symmetry(width, height, player_num):
    tiled = gen_2d_list(height, width)
    base_width = int((width + 1) / 2)

    # 基準プレイヤー配置　
    for cnt in range(player_num):
        x = randint(0, base_width - 1)
        y = randint(0, height - 1)
        player = int(player_num % 2 == 0 and cnt % 2 == 0) + 1
        while (tiled[y][x] != 0) and (tiled[y][x] == player):
            x = randint(0, base_width - 1)
            y = randint(0, height - 1)
        tiled[y][x] = player

    # 点対称に配置する
    for y in range(height):
        for x in range(base_width):
            tiled[height - y - 1][width - x - 1] = tiled[y][x]
            if (tiled[height - y - 1][width - x - 1] == 1) and (player_num % 2 == 1):
                tiled[height - y - 1][width - x - 1] = 2

    return deepcopy(tiled)
