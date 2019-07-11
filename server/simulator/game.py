from server.simulator.values import *

class Game:
    """
    Gameクラス

    Brief:
        ゲームを管理する

    Attributes:
        @__init__ (チャンネル名[str], 盤面情報[Board], エージェント情報[Agent: List])
            - コンストラクタ
        @set_action (チームID[int], エージェントID[int], アクション[MOVE_*, PANEL_*, STAY: int])
            - 行動決定
        @step ()
            - 1ターン進める
    """

    def __init__(self, channel, board, agents):
        self.channel = channel
        self.board = board
        self.agents = agents


    def set_action(self, team_id, agent_id, action):
        if (action < ACTION_ID_LOWER) or (ACTION_ID_UPPER < action):
            return False

        for agent in self.agents:
            if (agent.team == team_id) and (agent._id == agent_id):
                agent.action = action
                return True


    def step(self):
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


    def cal_mx_my(self, agent):
        action = ACTION[agent.action]
        mx = agent.x + action.dx
        my = agent.y + action.dy
        return (mx, my)


    def can_action(self, agent):
        mx, my = cal_mx_my(agent)
        return (0 <= mx) and (mx < self.board.width) and\
                    (0 <= my) and (my < self.board.height)
