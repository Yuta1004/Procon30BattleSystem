class Agent:
    def __init__(self, team, _id, x, y):
        self.team = team
        self._id = _id
        self.x = x
        self.y = y
        self.dx = -10
        self.dy = -10


class Board:
    def __init__(self, turn, width, height, points, tiled):
        self.turn = turn
        self.width = width
        self.height = height
        self.points = points
        self.tiled = tiled


class ActionInfo:
    def __init__(self, dx, dy, panel):
        self.dx = dx
        self.dy = dy
        self.panel = panel
