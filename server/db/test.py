from server.common.functions import dotest
from server.db.battle_db_manager import BattleDBAccessManager


def db_manager_test():
    # dotest("BattleDBAccessManagerTest1", battle_db_manager_test_1)
    dotest("BattleDBAccessManagerTest2", battle_db_manager_test_2)


def battle_db_manager_test_1():
    manager = BattleDBAccessManager()
    manager.insert("test_name", "test_token", 10, 30000, 1000, "teams_json")


def battle_db_manager_test_2():
    manager = BattleDBAccessManager()
    result = manager.get_data(1)
    keys = ["id", "name", "token", "turn", "turn_msec", "turn_switch_msec", "teams"]
    values = [1, "test_name", "test_token", 10, 30000, 1000, "teams_json", False]
    for key, val in zip(keys, values):
        assert (result[key] == val), "TestFailed"
