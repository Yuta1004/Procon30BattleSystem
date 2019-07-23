import json
from server.db.db_manager import DBAccessManager
from server.simulator.board import Board
from server.simulator.agent import Agent


class StageDBAccessManager(DBAccessManager):

    def __init__(self):
        super().__init__()


    def __del__(self):
        super().__del__()


    @DBAccessManager.db_execute
    def insert(self, cursor, battle_id, width, height, points, tiled, agent_pos):
        """
        Stageテーブルにデータを追加

        Params
        ----------
        battle_id : int
            試合ID
        width : int
            盤面のサイズ(幅)
        height : int
            盤面のサイズ(高さ)
        points : str
            配点情報JSON
        tiled : str
            陣地情報JSON
        agent_pos : str
            エージェント初期配置JSON
        """

        sql =\
        """
            insert into stage (battle_id, width, height, points, tiled, agent_pos)
            values(%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (battle_id, width, height, points, tiled, agent_pos))


    def get_stage_data(self, battle_id):
        """
        Stageテーブルから初期データを取得して盤面(Board)とエージェント情報(list)を返す

        Params
        ----------
        battle_id : int
            試合ID

        Return
        ----------
        Board
            盤面情報
        list(Agent)
            エージェント情報
        """

        # 盤面情報
        board_info = self.__get_data(battle_id)
        if board_info is None:
            return None
        width = board_info["width"]
        height = board_info["height"]
        points = json.loads(board_info["points"])["points"]
        tiled = json.loads(board_info["tiled"])["tiled"]
        agent_pos = json.loads(board_info["agent_pos"])["agent_pos"]
        board = Board(width, height, points, tiled)

        # エージェント情報
        agents = []
        for team in agent_pos.keys():
            for agent_id in agent_pos[team].keys():
                agent = agent_pos[team][agent_id]
                agents.append(Agent(
                    int(team),
                    int(agent_id),
                    agent["x"],
                    agent["y"]
                ))

        return board, agents


    @DBAccessManager.db_execute
    def __get_data(self, cursor, battle_id):
        """
        Stageテーブルからデータを取得

        Params
        ----------
        battle_id : int
            試合ID

        Return
        ----------
        レコード情報(dict)
        """

        sql = "select * from stage where battle_id=%s"
        cursor.execute(sql, (battle_id, ))
        result = cursor.fetchall()
        if len(result) > 0:
            return result[0]
        else:
            return None
