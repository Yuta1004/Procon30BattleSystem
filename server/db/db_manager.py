import os
import pymysql.cursors


class DBAccessManager:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="procon30",
            password=os.environ.get("MYSQL_PASSWORD"),
            db="procon30",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )


    def __del__(self):
        self.conn.close()


    def db_execute(deco_func):
        """
        DB操作用デコレータ
            - cursorオブジェクトが関数に渡されて、処理終了後は自動でcommitする
            - デコレートされるメソッドはDBAccessManagerを継承していること
            - デコレートされるメソッドは第一引数にself, 第二引数にcursorを持つこと
        """

        def db_execute_wrapper(self, *args, **kwargs):
            with self.conn.cursor() as cursor:
                deco_func(self, cursor, *args, **kwargs)
            self.conn.commit()
        return db_execute_wrapper
