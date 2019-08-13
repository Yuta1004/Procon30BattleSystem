import json
from server.common.functions import flatten_2d, gen_2d_list
from server.db.action_db_manager import ActionDBAccessManager

class Game:
    """
    Gameクラス

    Brief:
        　シミュレーター
    """

    def __init__(self, board, agents):
        """
        コンストラクタ

        Params
        ----------
        board : Board
            盤面情報
        agents : Agent + List
            エージェント情報
        """
        self.board = board
        self.agents = agents
        self.turn = 0


    def set_action(self, team_id, agent_id, dx, dy, remove_panel=False):
        """
        エージェントに行動をセット

        Params
        ----------
        team_id : int
            チームID
        agent_id : int
            エージェントID
        dx : int
        dy : int
        """
        if abs(dx) > 1 or abs(dy) > 1:
            return False

        for agent in self.agents:
            if (agent.team == team_id) and (agent.id == agent_id):
                agent.dx = dx
                agent.dy = dy
                agent.remove_panel = remove_panel
                return True


    def step(self):
        """
        1ターンゲームを進める

        Params
        ----------
        None

        Returns
        ----------
        safety_agents : list
            正常に行動できたエージェントのID
        affected_agents : list
            競合を起こしたエージェントのID
        """

        # エージェントの行動が影響する範囲をリストアップ
        affected_positions = []
        for agent in filter(lambda n: n.dx >= -1, self.agents):
            mx, my = self.__cal_mx_my(agent)
            affected_positions.append((mx, my))
            if self.__can_action(agent) and agent.remove_panel:
                affected_positions.append(agent.x, agent.y)

        # 影響がないエージェントを行動させる
        safety_agents = []
        affected_agents = []
        for agent in filter(lambda n: n.dx >= -1, self.agents):
            mx, my = self.__cal_mx_my(agent)
            if self.__can_action(agent) and (affected_positions.count((mx, my)) == 1):  # 競合確認
                agent.move()    # 行動
                safety_agents.append(agent.id)
                if agent.remove_panel:
                    self.board.tiled[my][mx] = 0
                else:
                    self.board.tiled[my][mx] = agent.team
            else:
                affected_agents.append(agent.id)

        # エージェントリセット
        list(map(lambda agent: agent.reset(), self.agents))

        self.turn += 1
        return safety_agents, affected_agents


    def cal_score(self, team_id_list):
        """
        スコアを計算する

        Params
        ----------
        team_id_list : int + List
            スコアを計算するチームIDのリスト

        Returns
        ----------
        map<int, int>
            チームIDがキー, スコアが値
        """
        score_list = {}

        for (idx, team_id) in enumerate(team_id_list):
            score_list[team_id] = {}

            # タイルポイント
            tiled_tmp = flatten_2d(self.board.tiled)
            points_flat = flatten_2d(self.board.points)
            score_list[team_id]["tilePoint"] = sum(map(lambda x, y: (x == team_id) * y, tiled_tmp, points_flat))

            # 全ての座標について、囲みが有効か探索
            self.rec_tiled = gen_2d_list(self.board.height, self.board.width)
            for y in range(self.board.height):
                for x in range(self.board.width):
                    if (self.rec_tiled[y][x] == 0) and (not self.__recursive_child(x, y, team_id)):
                        self.rec_tiled[y][x] = 0

            # 領域ポイント : 囲みが有効である座標のスコアを合計する
            self.rec_tiled = flatten_2d(self.rec_tiled)
            score_list[team_id]["areaPoint"] = sum(map(lambda x, y: abs(x * y), self.rec_tiled, points_flat))

        self.rec_tiled = None
        return score_list


    def __recursive_child(self, x, y, target):
        # 盤面の外周に来た = 囲み無効
        if (x == 0) or (x == self.board.width - 1) or (y == 0) or (y == self.board.height - 1):
            return False
        elif self.board.tiled[y][x] == target:
            return True
        else:
            self.rec_tiled[y][x] = 1

        # 4方向を調べる
        dx_list = [-1, 1, 0, 0]
        dy_list = [0, 0, -1, 1]
        for (dx, dy) in zip(dx_list, dy_list):
            mx = x + dx
            my = y + dy
            if self.__is_safe_pos(mx, my) and (self.rec_tiled[my][mx] == 0)\
                    and (self.board.tiled[my][mx] != target):
                if not self.__recursive_child(mx, my, target):
                    self.rec_tiled[my][mx] = 0
                    return False
        return True


    def __cal_mx_my(self, agent):
        mx = agent.x + agent.dx
        my = agent.y + agent.dy
        return mx, my


    def __can_action(self, agent):
        mx, my = self.__cal_mx_my(agent)
        return self.__is_safe_pos(mx, my)


    def __is_safe_pos(self, x, y):
        return (0 <= x) and (x < self.board.width) and\
                    (0 <= y) and (y < self.board.height)

