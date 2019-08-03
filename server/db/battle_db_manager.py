from copy import deepcopy
from server.db.db_manager import DBAccessManager


class BattleDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, name, start_at_unix_time, turn, turn_mills, interval_mills, teamA, teamB):
        """
        Battleテーブルにデータを挿入する

        Params
        ----------
        name : str
            試合名
        start_at_unix_time : int
            試合が始まるUNIX時間
        turn : int
            ターン数
        turn_mills : int
            1ターンの秒数(msec)
        interval_mills : int
            ターン切り替えの秒数(msec)
        teamA : int
            チームAのID
        teamB : int
            チームBのID

        Return
        ----------
        追加された試合のID
        """

        sql =\
        """
            insert into battle (name, start_at_unix_time, turn, turn_mills, interval_mills, teamA, teamB, now_battle)
            values(%s, %s, %s, %s, %s, %s, %s, 0)
        """
        cursor.execute(sql, (name, start_at_unix_time, turn, turn_mills, interval_mills, teamA, teamB))
        return cursor.lastrowid


    @DBAccessManager.db_execute
    def get_data(self, cursor, battle_id):
        """
        Battleテーブルからデータを取得する

        Params
        ----------
        battle_id
            試合ID

        Return
        ----------
        レコード情報(dict)
        """

        sql = "select * from battle where id=%s"
        cursor.execute(sql, (battle_id, ))
        result = cursor.fetchall()
        if len(result) > 0:
            result = result[0]
            result["now_battle"] = (True if result["now_battle"] == 1 else False)
            return result
        else:
            return None


    @DBAccessManager.db_execute
    def update_battle_status(self, cursor, status):
        """
        試合ステータスを更新する

        Params
        ----------
        status
            ステータス。1でゲーム開始前orゲーム中、0でゲーム終了を表す
        """

        sql = "update battle set now_battle=%s where id=%s"
        cursor.execute(sql, (status, ))
