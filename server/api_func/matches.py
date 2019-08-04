from server.db.team_db_manager import TeamDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager


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

    battle_db_manager = BattleDBAccessManager()
    team_db_manager = TeamDBAccessManager()
    team = team_db_manager.get_data(token=token)

    # トークン存在なし
    if team is None:
        return 401, {
            "status": "InvalidToken"
        }

    # 同じトークンを持つチーム一覧を抜き出し→そのチームが参戦しているチームを抜き出す
    match_list = []
    team = team[0]
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
