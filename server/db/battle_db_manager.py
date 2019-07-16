from server.db.db_manager import DBAccessManager


class BattleDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    @DBAccessManager.db_execute
    def insert(self, cursor, name, token, turn, turn_msec, turn_switch_msec, teams):
        sql =\
        """
            insert into battle (name, token, turn, turn_msec, turn_switch_msec, teams, now_battle)
            values(%s, %s, %s, %s, %s, %s, 0)
        """
        cursor.execute(sql, (name, token, turn, turn_msec, turn_switch_msec, teams))
