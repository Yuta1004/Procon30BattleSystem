import time
import datetime
import threading
from copy import deepcopy
from server.common.functions import flatten_2d
from server.db.team_db_manager import TeamDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager
from server.battle.battle_manager import BattleManager
from server.battle.action import save_action


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
    team_db_manager = TeamDBAccessManager()
    team = team_db_manager.get_data(token=token)
    if team is None:
        return 401, {
            "status": "InvalidToken"
        }

    # 試合参加チェック
    team = team[0]
    battle_db_manager = BattleDBAccessManager()
    battle = battle_db_manager.get_data(battle_id=battle_id)
    if (battle is None):
        return 400, {
            "startAtUnixTime": 0,
            "status": "InvalidMatches"
        }
    battle = battle[0]
    if (battle["teamA"] != team["id"]) and (battle["teamB"] != team["id"]):
        return 400, {
            "startAtUnixTime": 0,
            "status": "InvalidMathches"
        }

    # 試合開始前アクセス
    now_datetime = datetime.datetime.now()
    now_unix_time = int(time.mktime(now_datetime.timetuple()))
    if now_unix_time < battle["start_at_unix_time"]:
        return 400, {
            "startAtUnixTime": battle["start_at_unix_time"],
            "status": "TooEarly"
        }

    # インターバルチェック
    battle_manager = None
    for thread in threading.enumerate():
        if (type(thread) == BattleManager) and (thread.battle_id == battle_id):
            battle_manager = thread
            if thread.now_interval:
                return 400, {
                    "startAtUnixTime": battle["start_at_unix_time"],
                    "status": "UnacceptableTime"
                }

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
