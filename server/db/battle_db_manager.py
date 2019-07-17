from copy import deepcopy
from server.db.db_manager import DBAccessManager


class BattleDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, name, token, turn, turn_msec, turn_switch_msec, teams):
        """
        Battleテーブルにデータを挿入する

        Params
        ----------
        name : str
            試合名
        token : str
            トークン
        turn : int
            ターン数
        turn_msec : int
            1ターンの秒数(msec)
        turn_switch_msec : int
            ターン切り替えの秒数(msec)
        teams : str
            チーム情報JSON
        """

        sql =\
        """
            insert into battle (name, token, turn, turn_msec, turn_switch_msec, teams, now_battle)
            values(%s, %s, %s, %s, %s, %s, 0)
        """
        cursor.execute(sql, (name, token, turn, turn_msec, turn_switch_msec, teams))


    @DBAccessManager.db_execute
    def get_data(self, cursor, conditon_id):
        """
        Battleテーブルからデータを取得する

        Params
        ----------
        condition_id
            試合ID

        Return
        ----------
        レコード情報(dict)
        """

        sql = "select * from battle where id=%s"
        cursor.execute(sql, (conditon_id))
        result = cursor.fetchall()
        if len(result) > 0:
            result = result[0]
            result["now_battle"] = (True if result["now_battle"] == 1 else False)
            return result
        else:
            return None
