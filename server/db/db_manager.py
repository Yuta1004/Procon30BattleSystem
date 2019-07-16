import os
import pymysql.cursors


class DBAccessManager:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="procon30",
            password=os.environ.get("MYSQL_PASSWORD"),
            db="procon30",
            charset="utf8b4",
            cursorclass=pymysql.cursors.DictCursor
        )


    def db_execute(self, deco_func):
        """
        DB操作用デコレータ
        cursorオブジェクトが関数に渡されて、処理終了後は自動でcommitする
        """

        def db_execute_wrapper(*args, **kwargs):
            with self.conn.cursor() as cursor:
                deco_func(cursor, *args, **kwargs)
            self.conn.commit()
        return db_execute_wrapper
