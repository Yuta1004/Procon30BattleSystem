from server.db.db_manager import DBAccessManager


class ActionDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, battle_id, turn, detail):
        """
        Actionテーブルにデータを追加する

        Params
        ----------
        battle_id : int
            試合ID
        turn : int
            ターン
        detail : str
            行動情報JSON
        """

        sql =\
        """
            insert into action (battle_id, turn, detail)
            values(%s, %s, %s)
        """
        cursor.execute(sql, (battle_id, turn, detail))


    @DBAccessManager.db_execute
    def get_data(self, cursor, battle_id, turn=None):
        """
        Actionテーブルから指定ID、指定ターンのデータを取得する

        Params
        ----------
        battle_id : int
            試合ID
        turn : int
            ターン、指定しない場合は検索条件から除外

        Return
        ----------
        レコード情報(dict)のリスト
        """

        sql = "select * from action where battle_id=%s"
        req_tuple = (battle_id, )
        if turn is not None:
            sql += " and turn=%s"
            req_tuple = (battle_id, turn)
        cursor.execute(sql, req_tuple)
        result = cursor.fetchall()

        if len(result) > 0:
            return result
        else:
            return None


    @DBAccessManager.db_execute
    def update(self, cursor, battle_id, turn, action):
        sql = "update action set detail=%s where battle_id=%s and turn=%s"
        cursor.execute(sql, (action, battle_id, turn))


    @DBAccessManager.db_execute
    def count(self, cursor, battle_id, turn=None):
        sql = "select count(&) from action where battle_id=%s"
        req_tuple = (battle_id, )
        if turn is not None:
            sql += " and turn=%s"
            req_tuple = (battle_id, turn)
        cursor.execute(sql, req_tuple)
        return cursor.fetchall()[0]