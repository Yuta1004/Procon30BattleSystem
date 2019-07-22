import json
from server.simulator.board import generate_board, LINE_SYMMETRY_HALF
from server.db.battle_db_manager import BattleDBAccessManager
from server.db.stage_db_manager import StageDBAccessManager


def register(name, start_at_unix_time, turn, board_width, board_height,
             point_lower, point_upper, player_num, teamA, teamB,
             generate_board_type=LINE_SYMMETRY_HALF,
             turn_mills=30000, interval_mills=3000):
    board = generate_board(
        turn,
        board_width,
        board_height,
        point_upper,
        point_lower,
        player_num,
        generate_board_type
    )

    battle_db_manager = BattleDBAccessManager()
    battle_id = battle_db_manager.insert(
        name,
        start_at_unix_time,
        turn,
        turn_mills,
        interval_mills,
        teamA,
        teamB
    )

    stage_db_manager = StageDBAccessManager()
    stage_db_manager.insert(
        battle_id,
        board_width,
        board_height,
        json.dumps({"points": board.points}),
        json.dumps({"tiled": board.tiled})
    )

    return battle_id
