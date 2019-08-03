import json
import time
import datetime
from threading import Thread
from server.simulator.board import Board
from server.simulator.game import Game
from server.simulator.agent import Agent
from server.db.action_db_manager import ActionDBAccessManager
from server.db.stage_db_manager import StageDBAccessManager
from server.db.battle_db_manager import BattleDBAccessManager


class BattleManager(Thread):

    def __init__(self, battle_id):
        super().__init__()
        self.game = None
        self.battle_id = battle_id
        self.__roll_forward()


    def run(self):
        # 0. 準備
        battle_db_manager = BattleDBAccessManager()
        battle_data = battle_db_manager.get_data(self.battle_id)
        turn_limit = battle_data["turn"]
        turn_mills = battle_data["turn_mills"]
        interval_mills = ["interval_mills"]
        msleep = lambda t: time.sleep(t / 1000.0)

        # 1. 試合開始待機
        self.__wait_for_start_battle()

        # 2. 試合プロセス
        for turn in range(1, turn_limit + 1):
            # 送信待機
            msleep(turn_mills)
            before_time = int(time.time() * 1000)

            # 行動
            action_db_manager = ActionDBAccessManager()
            action = action_db_manager.get_data(self.battle_id, turn)
            action = json.loads(action["detail"])["detail"]
            self.__do_action(action)

            # 次ターンまで待機
            after_time = int(time.time() * 1000)
            while before_time + interval_mills > after_time:
                after_time = int(time.time() * 1000)


    def __wait_for_start_battle(self):
        unix_time = -1
        battle_db_manager = BattleDBAccessManager()
        start_at_unix_time = battle_db_manager.get_data(self.battle_id)["start_at_unix_time"]
        del(start_at_unix_time)

        while unix_time != start_at_unix_time:
            now_datetime = datetime.datetime.now()
            unix_time = int(time.mktime(now_datetime.timetuple()))


    def __roll_forward(self):
        # 盤面情報
        stage_manager = StageDBAccessManager()
        board, agents = stage_manager.get_stage_data(self.battle_id)
        self.game = Game(board, agents)

        # 行動履歴取得
        action_manager = ActionDBAccessManager()
        action_history = action_manager.get_data(self.battle_id)
        action_history = sorted(action_history, key=lambda x: x["turn"])

        # 盤面復元
        for action in action_history:
            self.__do_action(json.loads(action["detail"])["detail"])


    def __do_action(self, action_detail):
        for agent in action_detail:
            team_id = agent["team_id"]
            agent_id = agent["agent_id"]
            remove_panel = agent["type"] == "remove"
            dx = agent["dx"]
            dy = agent["dy"]
            self.game.set_action(team_id, agent_id, dx, dy, remove_panel)
        self.game.simulator.step()
