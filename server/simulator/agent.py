class Agent:
    def __init__(self, team, _id, x, y):
        self.team = team
        self._id = _id
        self.x = x
        self.y = y
        self.action = -1
        self.dx = -10
        self.dy = -10
