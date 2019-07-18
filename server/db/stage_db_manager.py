from server.db.db_manager import DBAccessManager


class StageDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, battle_id, width, height, points, tiled):
        """
        Stageテーブルにデータを追加

        Params
        ----------
        battle_id : int
            試合ID
        width : int
            盤面のサイズ(幅)
        height : int
            盤面のサイズ(高さ)
        points : str
            配点情報JSON
        tiled : str
            陣地情報JSON
        """

        sql =\
        """
            insert into stage (battle_id, width, height, points, tiled)
            values(%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (battle_id, width, height, points, tiled))


    @DBAccessManager.db_execute
    def get_data(self, cursor, battle_id):
        """
        Stageテーブルからデータを取得

        Params
        ----------
        battle_id : int
            試合ID

        Return
        ----------
        レコード情報(dict)
        """

        sql = "select * from stage where battle_id=%s"
        cursor.execute(sql, (battle_id, ))
        result = cursor.fetchall()
        if len(result) > 0:
            return result[0]
        else:
            return None
