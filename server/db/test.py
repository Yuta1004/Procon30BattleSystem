from server.common.functions import dotest
from server.db.battle_db_manager import BattleDBAccessManager


def db_manager_test():
    # dotest("BattleDBAccessManagerTest 1", battle_db_manager_test_1)
    pass


def battle_db_manager_test_1():
    manager = BattleDBAccessManager()
    manager.insert("test_name", "test_token", 10, 30000, 1000, "teams_json")
