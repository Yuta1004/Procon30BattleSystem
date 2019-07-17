from server.db.db_manager import DBAccessManager


class StageDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, battle_id, points, tiled):
        sql =\
        """
            insert into stage (battle_id, points, tiled)
            values(%s, %s, %s)
        """
        cursor.execute(sql, (battle_id, points, tiled))


    @DBAccessManager.db_execute
    def get_data(self, cursor, battle_id):
        sql = "select * from stage where battle_id=%s"
        cursor.execute(sql, (battle_id, ))
        result = cursor.fetchall()
        if len(result) > 0:
            return result[0]
        else:
            return None
