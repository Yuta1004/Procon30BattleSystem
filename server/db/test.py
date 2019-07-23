import random
import json
from server.common.functions import dotest
from server.db.battle_db_manager import BattleDBAccessManager
from server.db.action_db_manager import ActionDBAccessManager
from server.db.stage_db_manager import StageDBAccessManager
from server.db.team_db_manager import TeamDBAccessManager


def db_manager_test():
    # dotest("TeamDBAccessManagerTest1", team_db_manager_test_1)
    dotest("TeamDBAccessManagerTest2", team_db_manager_test_2)
    dotest("TeamDBAccessManagerTest3", team_db_manager_test_3)
    dotest("TeamDBAccessManagerTest4", team_db_manager_test_4)

    # dotest("BattleDBAccessManagerTest1", battle_db_manager_test_1)
    dotest("BattleDBAccessManagerTest2", battle_db_manager_test_2)

    # dotest("ActionDBAccessManagerTest1", action_db_manager_test_1)
    dotest("ActionDBAccessManagerTest2", action_db_manager_test_2)
    dotest("ActionDBAccessManagerTest3", action_db_manager_test_3)
    dotest("ActionDBAccessManagerTest4", action_db_manager_test_4)
    dotest("ActionDBAccessManagerTest5", action_db_manager_test_4)
    dotest("ActionDBAccessManagerTest6", action_db_manager_test_4)

    # dotest("StageDBAccessManagerTest1", stage_db_manager_test_1)
    dotest("StageDBAccessManagerTest2", stage_db_manager_test_2)


def team_db_manager_test_1():
    manager = TeamDBAccessManager()
    manager.insert("teamA", "test_tokenA")
    manager.insert("teamB", "test_tokenB")


def team_db_manager_test_2():
    manager = TeamDBAccessManager()
    result = manager.get_data(1)[0]
    assert(result["id"] == 1)
    assert(result["name"] == "teamA")
    assert(result["token"] == "test_tokenA")


def team_db_manager_test_3():
    manager = TeamDBAccessManager()
    result = manager.get_data(token="test_tokenA")[0]
    assert(result["id"] == 1)
    assert(result["name"] == "teamA")
    assert(result["token"] == "test_tokenA")


def team_db_manager_test_4():
    manager = TeamDBAccessManager()
    result = manager.get_data(1, "test_tokenA")[0]
    assert(result["id"] == 1)
    assert(result["name"] == "teamA")
    assert(result["token"] == "test_tokenA")


def battle_db_manager_test_1():
    manager = BattleDBAccessManager()
    manager.insert("test_name", 0, 10, 30000, 1000, 1, 2)


def battle_db_manager_test_2():
    manager = BattleDBAccessManager()
    result = manager.get_data(1)
    keys = ["id", "name", "start_at_unix_time", "turn", "turn_mills",
            "interval_mills", "teamA", "teamB", "now_battle"]
    values = [1, "test_name", 0, 10, 30000, 1000, 1, 2, False]
    for key, val in zip(keys, values):
        assert(result[key] == val)


def action_db_manager_test_1():
    manager = ActionDBAccessManager()
    manager.insert(1, 1, "test_action")


def action_db_manager_test_2():
    manager = ActionDBAccessManager()
    tmp_action = str(random.randint(0, 1<<30))
    # 1
    manager.update(1, 1, tmp_action)
    result = manager.get_data(1, 1)[0]
    assert(result["detail"] == tmp_action)
    # 2
    manager.update(1, 1, "test_action")
    result = manager.get_data(1, 1)[0]
    assert(result["detail"] == "test_action")


def action_db_manager_test_3():
    manager = ActionDBAccessManager()
    result = manager.get_data(1)[0]
    keys = ["battle_id", "turn", "detail"]
    values = [1, 1, "test_action"]
    for key, val in zip(keys, values):
        assert(result[key] == val)


def action_db_manager_test_4():
    manager = ActionDBAccessManager()
    result = manager.get_data(1, 1)
    keys = ["battle_id", "turn", "detail"]
    values = [1, 1, "test_action"]
    for item in result:
        for key, val in zip(keys, values):
            assert(item[key] == val)


def action_db_manager_test_5():
    manager = ActionDBAccessManager()
    assert(manager.count(1, 1) == 1)


def action_db_manager_test_6():
    manager = ActionDBAccessManager()
    assert(manager.count(1) == 1)


def stage_db_manager_test_1():
    manager = StageDBAccessManager()
    manager.insert(
        1,
        2,
        2,
        json.dumps({"points": [[1, 2], [3, 4]]}),
        json.dumps({"tiled": [[1, 2], [3, 4]]}),
        json.dumps({
            "agent_pos": {
                1: {
                    1: {"x": 0, "y": 0},
                    2: {"x": 1, "y": 0}
                },
                2: {
                    3: {"x": 0, "y": 1},
                    4: {"x": 1, "y": 1}
                }
            }
        })
    )


def stage_db_manager_test_2():
    manager = StageDBAccessManager()
    board, agents = manager.get_stage_data(1)
    assert(board.width == 2)
    assert(board.height == 2)
    assert(board.tiled == [[1, 2], [3, 4]])
    assert(board.points == [[1, 2], [3, 4]])
    for agent in agents:
        assert(type(agent.team) == int)
        assert(type(agent.id) == int)
