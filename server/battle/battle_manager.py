import math
import json
import time
import datetime
import threading
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
        self.turn = 1
        self.max_turn = 9999999
        self.battle_id = battle_id
        self.now_interval = False
        self.action_writing = False
        self.battle_info = BattleDBAccessManager().get_data(battle_id=self.battle_id)[0]
        self.finish_battle = threading.Event()

        self.__roll_forward()
        BattleDBAccessManager().update_battle_status(self.battle_id, 1)


    def run(self):
        # 0. 準備
        battle_db_manager = BattleDBAccessManager()
        battle_data = battle_db_manager.get_data(battle_id=self.battle_id)[0]
        turn_limit = battle_data["turn"]
        turn_mills = battle_data["turn_mills"]
        interval_mills = battle_data["interval_mills"]
        msleep = lambda t: time.sleep(t / 1000.0)
        del(battle_db_manager)

        # 1. 試合開始待機
        self.__wait_for_start_battle()

        # 2. 試合プロセス
        self.turn = max(1, self.turn)
        for self.turn in range(self.turn, turn_limit + 1):
            # 送信待機
            msleep(turn_mills)
            while self.action_writing:
                pass
            before_time = int(time.time() * 1000)

            # 行動準備
            self.now_interval = True
            action_db_manager = ActionDBAccessManager()
            action = action_db_manager.get_data(self.battle_id, self.turn)

            # 行動 -> エージェントステータス更新
            if len(action) != 0:
                action = json.loads(action[0]["detail"])["actions"]
                safety_agents, affected_agents = self.__do_action(action)
                for agent in action:
                    if agent["agent_id"] in safety_agents:
                        agent["apply"] = 1
                    elif agent["agent_id"] in affected_agents:
                        agent["apply"] = 0
                action_db_manager.update(self.battle_id, self.turn, json.dumps({"actions": action}))

            # 次ターンまで待機
            after_time = int(time.time() * 1000)
            while before_time + interval_mills > after_time:
                after_time = int(time.time() * 1000)
            self.now_interval = False

            # 終了コマンドを受け取ったら
            if self.finish_battle.is_set():
                break

        # 3. 終了コマンド待機
        self.turn = self.max_turn + 1
        while not self.finish_battle.is_set():
            time.sleep(10)
        BattleDBAccessManager().update_battle_status(self.battle_id, 0)


    def get_board(self):
        return self.game.board


    def get_agents(self):
        return self.game.agents


    def get_score(self):
        return self.game.cal_score(
            [self.battle_info["teamA"], self.battle_info["teamB"]]
        )


    def finish(self):
        self.finish_battle.set()


    def __wait_for_start_battle(self):
        now_datetime = datetime.datetime.now()
        unix_time = int(time.mktime(now_datetime.timetuple()))
        battle_db_manager = BattleDBAccessManager()
        start_at_unix_time = battle_db_manager.get_data(battle_id=self.battle_id)[0]["start_at_unix_time"]
        del(battle_db_manager)

        while unix_time < start_at_unix_time:
            now_datetime = datetime.datetime.now()
            unix_time = int(time.mktime(now_datetime.timetuple()))


    def __roll_forward(self):
        # 盤面情報
        stage_manager = StageDBAccessManager()
        board, agents = stage_manager.get_stage_data(self.battle_id)
        self.game = Game(board, agents)

        # 行動履歴取得
        action_manager = ActionDBAccessManager()
        action_history = action_manager.get_data(battle_id=self.battle_id)
        action_history = sorted(action_history, key=lambda x: x["turn"])

        # 盤面復元
        battle_info = BattleDBAccessManager().get_data(self.battle_id)[0]
        for action in action_history:
            if action["turn"] <= battle_info["turn"]:
                self.__do_action(json.loads(action["detail"])["actions"])

        # ターン情報復元
        ## 試合が開始してからの秒数を計算
        start_at_unix_time = battle_info["start_at_unix_time"]
        now_unix_time = int(time.mktime(datetime.datetime.now().timetuple()))
        passed_time_millis = (now_unix_time - start_at_unix_time) * 1000

        ## 1ターンに要する時間で割る = 現在時刻でのターン数
        period_time_millis = battle_info["turn_mills"] + battle_info["interval_mills"]
        self.turn = math.ceil(passed_time_millis / period_time_millis)
        self.turn = max(0, min(battle_info["turn"] + 1, self.turn))
        self.max_turn = battle_info["turn"]

        ## 少し待機(復元ターンと現在時刻のずれを修正する)
        wait_millis = self.turn * period_time_millis - now_unix_time * 1000
        time.sleep(max(0, wait_millis / 1000.0))


    def __do_action(self, action_detail):
        for agent in action_detail:
            team_id = agent["team_id"]
            agent_id = agent["agent_id"]
            remove_panel = agent["type"] == "remove"
            dx = agent["dx"]
            dy = agent["dy"]
            self.game.set_action(team_id, agent_id, dx, dy, remove_panel)
        return self.game.step()
