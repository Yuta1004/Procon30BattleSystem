from server.db.db_manager import DBAccessManager


class TeamDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, name, token):
        """
        チームテーブルにデータを追加

        Params
        ----------
        name : str
            チーム名
        token : str
            トークン(一意なもの)
        """

        sql = "insert into team (name, token) values(%s, %s)"
        cursor.execute(sql, (name, token))


    @DBAccessManager.db_execute
    def get_data(self, cursor, team_id=None, token=None):
        """
        チームテーブルからデータを取得する

        Params
        ----------
        team_id : int
            チームID
        token : str
            トークン

        Return
        ----------
        list(dict)
        検索条件に一致するレコードの配列
        """

        sql = "select * from team where "
        req_tuple = (team_id, )

        # 設定された引数に応じて処理を変える
        if (team_id is None) and (token is None):
            raise ValueError("Must be set parameter [team_id] or [token]")
        elif (team_id is not None) and (token is not None):
            sql += "id=%s and token=%s"
            req_tuple = (team_id, token)
        elif token is not None:
            sql += "token=%s"
            req_tuple = (token, )
        else:
            sql += "id=%s"
            req_tuple = (team_id)

        cursor.execute(sql, req_tuple)
        result = cursor.fetchall()
        if len(result) > 0:
            return result
        else:
            return []
