from server.db.db_manager import DBAccessManager


class StageDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()
