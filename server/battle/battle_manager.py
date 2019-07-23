import json
from threading import Thread
from server.simulator.board import Board
from server.simulator.game import Game
from server.simulator.agent import Agent
from server.db.action_db_manager import ActionDBAccessManager
from server.db.stage_db_manager import StageDBAccessManager


class BattleManager(Thread):

    def __init__(self, battle_id):
        super().__init__()
        self.game = None
        self.battle_id = battle_id
        self.__roll_forward()


    def run(self):
        pass


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
