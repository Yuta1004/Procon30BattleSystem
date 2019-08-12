import json
import threading
from server.db.team_db_manager import TeamDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager
from server.db.action_db_manager import ActionDBAccessManager
from server.api_func.check import token_check, battle_join_check, battle_started_check
from server.battle.battle_manager import BattleManager


# /matches
def get_all_matches(token):
    """
    トークンを元に試合情報を返す

    Params
    ----------
    token : str
        トークン

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

    battle_db_manager = BattleDBAccessManager()
    team_db_manager = TeamDBAccessManager()
    team = team_db_manager.get_data(token=token)[0]

    # 同じトークンを持つチーム一覧を抜き出し→そのチームが参戦しているチームを抜き出す
    match_list = []
    for battle in battle_db_manager.get_data(team_id=team["id"]):
        match_team = battle["teamA"] if battle["teamB"] == team["id"] else battle["teamB"]
        match_list.append(
            {
                "id": battle["id"],
                "intervalMillis": battle["interval_mills"],
                "matchTo": team_db_manager.get_data(match_team)[0]["name"],
                "teamID": team["id"],
                "turnMillis": battle["turn_mills"],
                "turns": battle["turn"]
            }
        )
    return 200, match_list


#/matches/{id}
def get_match_detail(token, battle_id):
    # トークンチェック
    is_error, status, response = token_check(token)
    if is_error:
        return status, response

    # 試合参加チェック
    is_error, status, response = battle_join_check(token, battle_id)
    if is_error:
        return status, response

    # 試合開始チェック
    is_error, status, response = battle_started_check(battle_id)
    if is_error:
        return status, response

    # BattleManager取得
    battle_manager = None
    for thread in threading.enumerate():
        if (type(thread) == BattleManager) and (thread.battle_id == battle_id):
            battle_manager = thread
    if battle_manager is None:
        return 500, {"status": "Battle not started."}

    ret_dict = {}

    # width, height, points, tiled, turn, startAtUnixTime
    board = battle_manager.get_board()
    ret_dict["width"] = board.width
    ret_dict["height"] = board.height
    ret_dict["points"] = board.points
    ret_dict["tiled"] = board.tiled
    ret_dict["turn"] = battle_manager.turn
    ret_dict["startedAtUnixTime"] = battle_manager.battle_info["start_at_unix_time"]

    # teams
    teams = []
    score = battle_manager.get_score()
    for team_id in score.keys():
        team_agents = list(filter(lambda agent: agent.team == team_id, battle_manager.get_agents()))
        teams.append(
            {
                "teamID": team_id,
                "areaPoint": score[team_id]["areaPoint"],
                "tilePoint": score[team_id]["tilePoint"],
                "agents": list(map(lambda agent:
                    {
                        "agentID": agent.id,
                        "x": agent.x,
                        "y": agent.y
                    }
                    , team_agents))
            }
        )
    ret_dict["teams"] = teams

    # actions
    actions = []
    action_history = ActionDBAccessManager().get_data(battle_id)
    action_history = list(map(lambda action: json.loads(action["detail"])["actions"], action_history))
    for action in action_history:
        actions.extend(
            list(map(lambda x:
                {
                    "agentID": x["agent_id"],
                    "dx": x["dx"],
                    "dy": x["dy"],
                    "type": x["type"],
                    "apply": x["apply"],
                    "turn": x["turn"]
                }
            , action))
        )
    ret_dict["actions"] = actions

    return 200, ret_dict
