import json
from server.simulator.board import generate_board, LINE_SYMMETRY_HALF
from server.db.battle_db_manager import BattleDBAccessManager
from server.db.stage_db_manager import StageDBAccessManager


def battle_register(name, start_at_unix_time, turn, board_width, board_height,
             point_lower, point_upper, player_num, teamA, teamB,
             generate_board_type=LINE_SYMMETRY_HALF,
             turn_mills=30000, interval_mills=3000):
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

    board = generate_board(
        board_width,
        board_height,
        point_upper,
        point_lower,
        player_num,
        generate_board_type
    )

    board.tiled, agent_pos_dict = _get_agent_pos(
        battle_id,
        board.tiled,
        board_width,
        board_height,
        teamA,
        teamB
    )

    stage_db_manager = StageDBAccessManager()
    stage_db_manager.insert(
        battle_id,
        board_width,
        board_height,
        json.dumps({"points": board.points}),
        json.dumps({"tiled": board.tiled}),
        json.dumps({"agent_pos": agent_pos_dict})
    )

    return battle_id


def _get_agent_pos(battle_id, tiled, width, height, teamA, teamB):
    agent_pos_dict = {teamA: {}, teamB: {}}
    team_cnt = [0, 0]
    team_list = [teamA, teamB]

    # エージェントの座標チェック
    for y in range(height):
        for x in range(width):
            if tiled[y][x] > 0:
                team_idx = tiled[y][x] - 1
                agent_id = int(
                    str(battle_id % 2048) +\
                    str(team_list[team_idx] % 2048) +\
                    str(team_cnt[team_idx])
                )
                tiled[y][x] = agent_id
                team_cnt[team_idx] += 1
                agent_pos_dict[team_list[team_idx]][agent_id] = {
                    "x": x, "y": y
                }

    return tiled, agent_pos_dict
