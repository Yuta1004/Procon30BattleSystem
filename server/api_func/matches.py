from server.db.team_db_manager import TeamDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager
from server.api_func.check import token_check


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
