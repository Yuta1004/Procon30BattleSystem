from server.simulator.values import *
from server.common.functions import flatten_2d, gen_2d_list

class Game:
    """
    Gameクラス

    Brief:
        ゲームを管理する
    """

    def __init__(self, channel, board, agents):
        """
        コンストラクタ

        Params
        ----------
        channel : str
            チャンネル
        board : Board
            盤面情報
        agents : Agent + List
            エージェント情報
        """
        self.channel = channel
        self.board = board
        self.agents = agents


    def set_action(self, team_id, agent_id, action):
        """
        エージェントに行動をセット

        Params
        ----------
        team_id : int
            チームID
        agent_id : int
            エージェントID
        action : int
            アクション(values.pyにある定数を使うこと)
        """
        if (action < ACTION_ID_LOWER) or (ACTION_ID_UPPER < action):
            return False

        for agent in self.agents:
            if (agent.team == team_id) and (agent._id == agent_id):
                agent.action = action
                return True


    def step(self):
        """
        1ターンゲームを進める

        Params
        ----------
        None
        """
        # エージェントの行動が影響する範囲をリストアップ
        affected_positions = []
        for agent in filter(lambda n: n.action >= 0, self.agents):
            mx, my = cal_mx_my(agent)
            affected_positions.append((mx, my))
            if can_action(agent) and (ACTION[agent.action].panel == 1):
                affected_positions.append(agent.x, agent.y)

        # 影響がないエージェントを行動させる
        for agent in filter(lambda n: n.action >= 0, self.agents):
            mx, my = cal_mx_my(agent)
            action = ACTION[agent]
            if can_action(agent) and ((mx, my) not in affected_positions):
                if action.panel == 0:
                    self.board.tiled[my][mx] = agent.team
                elif action.panel == 1:
                    self.board.tiled[my][mx] = 0

        self.turn += 1


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
            # タイルポイント
            tiled_tmp = flatten_2d(self.board.tiled)
            points_flat = flatten_2d(self.board.points)
            score_list[team_id] = sum(map(lambda x, y: (x == team_id) * y, tiled_tmp, points_flat))

            # 全ての座標について、囲みが有効か探索
            self.rec_tiled = gen_2d_list(self.board.height, self.board.width)
            for y in range(self.board.height):
                for x in range(self.board.width):
                    if (self.rec_tiled[y][x] == 0) and (not self.recursive_child(x, y, team_id)):
                        self.rec_tiled[y][x] = 0

            # 領域ポイント : 囲みが有効である座標のスコアを合計する
            self.rec_tiled = flatten_2d(self.rec_tiled)
            score_list[team_id] += sum(map(lambda x, y: abs(x * y), self.rec_tiled, points_flat))

        self.rec_tiled = None
        return score_list


    def recursive_child(self, x, y, target):
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
            if self.is_safe_pos(mx, my) and (self.rec_tiled[my][mx] == 0)\
                    and (self.board.tiled[my][mx] != target):
                if not self.recursive_child(mx, my, target):
                    self.rec_tiled[my][mx] = 0
                    return False
        return True


    def cal_mx_my(self, agent):
        action = ACTION[agent.action]
        mx = agent.x + n.dx
        my = agent.y
        return mx, my


    def can_action(self, agent):
        mx, my = cal_mx_my(agent)
        return is_safe_pos(mx, my)


    def is_safe_pos(self, x, y):
        return (0 <= x) and (x < self.board.width) and\
                    (0 <= y) and (y < self.board.height)

