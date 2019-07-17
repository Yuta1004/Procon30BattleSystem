from server.db.db_manager import DBAccessManager


class ActionDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()
