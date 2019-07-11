from server.simulator.data import ActionInfo

# Move Const Values
MOVE_UP = 0
MOVE_RIGHT_UP = 1
MOVE_RIGHT = 2
MOVE_RIGHT_DOWN = 3
MOVE_DOWN = 4
MOVE_LEFT_DOWN = 5
MOVE_LEFT_LEFT = 6
MOVE_LEFT = 7

# Panel Const Values
PANEL_UP = 8
PANEL_RIGHT_UP = 9
PANEL_RIGHT = 10
PANEL_RIGHT_DOWN = 11
PANEL_DOWN = 12
PANEL_LEFT_DOWN = 13
PANEL_LEFT_LEFT = 14
PANEL_LEFT = 15

# Actions
ACTION = [] * 16

ACTION[MOVE_UP] = ActionInfo(0, -1, 0)
ACTION[MOVE_RIGHT_UP] = ActionInfo(1, -1, 0)
ACTION[MOVE_RIGHT] = ActionInfo(1, 0, 0)
ACTION[MOVE_RIGHT_DOON] = ActionInfo(1, 1, 0)
ACTION[MOVE_DOWN] = ActionInfo(0, 1, 0)
ACTION[MOVE_LEFT_DOWN] = ActionInfo(-1, 1, 0)
ACTION[MOVE_LEFT] = ActionInfo(-1, 0, 0)
ACTION[MOVE_LEFT_UP] = ActionInfo(-1, -1, 0)

ACTION[PANEL_UP] = ActionInfo(0, -1, 1)
ACTION[PANEL_RIGHT_UP] = ActionInfo(1, -1, 1)
ACTION[PANEL_RIGHT] = ActionInfo(1, 0, 1)
ACTION[PANEL_RIGHT_DOON] = ActionInfo(1, 1, 1)
ACTION[PANEL_DOWN] = ActionInfo(0, 1, 1)
ACTION[PANEL_LEFT_DOWN] = ActionInfo(-1, 1, 1)
ACTION[PANEL_LEFT] = ActionInfo(-1, 0, 1)
ACTION[PANEL_LEFT_UP] = ActionInfo(-1, -1, 1)