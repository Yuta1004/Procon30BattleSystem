import time
import datetime
import threading
from server.db.team_db_manager import TeamDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager
from server.battle.battle_manager import BattleManager


def token_check(token):
    """
    トークン確認チェック

    Params
    ----------
    token : str
        トークン

    Return
    ----------
    bool
        エラーの有無
    int
        エラーがあった場合、そのHTTPステータス
    dict or list
        エラーがあった場合、その内容
    """

    token_check = TeamDBAccessManager().get_data(token=token)
    if token_check is None:
        return True, 401, {"status": "InvalidToken"}
    else:
        return False, None, None


def battle_join_check(token, battle_id):
    """
    試合に参加しているかチェック

    Params
    ----------
    token : str
        トークン
    battle_id : int
        試合ID

    Returns
    ----------
    bool
        エラーの有無
    int
        エラーがあった場合、そのHTTPステータス
    dict or list
        エラーがあった場合、その内容
    """

    team = TeamDBAccessManager().get_data(token=token)[0]
    battle_db_manager = BattleDBAccessManager()
    battle = BattleDBAccessManager().get_data(battle_id=battle_id)
    if (battle is None):
        return True, 400, {
            "startAtUnixTime": 0,
            "status": "InvalidMatches"
        }
    battle = battle[0]
    if (battle["teamA"] != team["id"]) and (battle["teamB"] != team["id"]):
        return True, 400, {
            "startAtUnixTime": 0,
            "status": "InvalidMathches"
        }

    return False, None, None


def battle_started_check(battle_id):
    """
    試合が開始されているか確認

    Params
    ----------
    battle : int
        試合ID

    Returns
    ----------
    bool
        エラーの有無
    int
        エラーがあった場合、そのHTTPステータス
    dict or list
        エラーがあった場合、その内容
    """

    battle = BattleDBAccessManager().get_data(battle_id=battle_id)[0]
    now_datetime = datetime.datetime.now()
    now_unix_time = int(time.mktime(now_datetime.timetuple()))
    if now_unix_time < battle["start_at_unix_time"]:
        return True, 400, {
            "startAtUnixTime": battle["start_at_unix_time"],
            "status": "TooEarly"
        }

    return False, None, None

def interval_check(battle_id):
    """
    指定された試合がインターバル中かチェック

    Params
    ----------
    battle_id : int
        試合ID

    Returns
    ----------
    bool
        エラーの有無
    int
        エラーがあった場合、そのHTTPステータス
    dict or list
        エラーがあった場合、その内容
    BattleManager
        当該BattleManager
    """

    battle = BattleDBAccessManager().get_data(battle_id=battle_id)[0]
    battle_manager = None
    for thread in threading.enumerate():
        if (type(thread) == BattleManager) and (thread.battle_id == battle_id):
            battle_manager = thread
            if thread.now_interval:
                return True, 400, {
                    "startAtUnixTime": battle["start_at_unix_time"],
                    "status": "UnacceptableTime"
                }, battle_manager

    return False, None, None, battle_manager
