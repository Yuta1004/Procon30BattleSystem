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
    dict or list
        レスポンスデータ
    """

    battle_db_manager = BattleDBAccessManager()
    team_db_manager = TeamDBAccessManager()
    team_list = team_db_manager.get_data(token=token)

    # トークン存在なし
    if len(team_list) == 0:
        return {
            "status": "InvalidToken"
        }

    # 同じトークンを持つチーム一覧を抜き出し→そのチームが参戦しているチームを抜き出す
    match_list = []
    for team in team_list:
        for battle in battle_db_manager.get_data(token=team["id"]):
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
    return match_list
