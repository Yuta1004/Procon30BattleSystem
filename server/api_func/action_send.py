import time
import datetime
import threading
from copy import deepcopy
from server.common.functions import flatten_2d
from server.db.team_db_manager import TeamDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager
from server.battle.battle_manager import BattleManager
from server.battle.action import save_action
from server.api_func.check import token_check, battle_join_check, battle_started_check, interval_check


def action_send(token, battle_id, action_list):
    """
    トークンや行動情報JSONを元に行動を保存する

    Params
    ----------
    token : str
        トークン
    battle_id : int
        試合ID
    action_list : list
        行動情報

    Returns
    ----------
    int
        HTTPステータス
    dict or list
        レスポンスデータ
    """

    # トークンチェック
    is_error, status, response = token_check(token)
    if is_error:
        return status, response

    # 試合参加チェック
    is_error, status, response = battle_join_check(token, battle_id)
    if is_error:
        return status, response

    # 試合開始前アクセス
    is_error, status, response = battle_started_check(battle_id)
    if is_error:
        return status, response

    # インターバルチェック
    is_error, status, response, battle_manager = interval_check(battle_id)
    if is_error:
        return status, response

    # 行動保存
    while battle_manager.action_writing: pass
    battle_manager.action_writing = True
    action_list = []
    turn = battle_manager.turn
    for action in action_list:
        agent_id = action["agentID"]
        dx = action["dx"]
        dy = action["dy"]
        action_type = action["type"]
        action["turn"] = turn
        save_action(battle_id, token, turn, agent_id, action_type, dx, dy)  # 行動書き込み!
        action_list.append(deepcopy(action))
    battle_manager.action_writing = False

    return 200, {
        "actions": action_list
    }
