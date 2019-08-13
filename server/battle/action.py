import json
from server.db.action_db_manager import ActionDBAccessManager
from server.db.team_db_manager import TeamDBAccessManager


def save_action(battle_id, token, turn, agent_id, action_type, dx, dy):
    if action_type not in ["move", "remove", "stay"]:
        raise ValueError(
            "action_type must be one of [\"move\", \"remove\", \"stay\"]"
        )
    if abs(dx) > 1 or abs(dy) > 1:
        raise ValueError(
            "(dx, dy) must be in the range -1 to 1"
        )

    # トークンを元にしてチームIDを取得
    team_id = TeamDBAccessManager().get_data(token=token)[0]["id"]
    # 指定されたID,ターンにまだ行動が登録されていなかった場合 or そうでない場合
    manager = ActionDBAccessManager()
    if manager.count(battle_id, turn) == 0:
        manager.insert(
            battle_id,
            turn,
            json.dumps({
                "actions": [
                    {
                        "team_id": team_id,
                        "agent_id": agent_id,
                        "type": action_type,
                        "dx": dx,
                        "dy": dy,
                        "turn": turn,
                        "apply": -1
                    }
                ]
            })
        )
    else:
        actions = json.loads(manager.get_data(battle_id, turn)[0]["detail"])
        # 指定agent_idの行動が既に指定されていた場合 or そうでない場合
        if len(list(filter(lambda x: x["agent_id"] == agent_id, actions["actions"]))) >= 1:
            for action in actions["actions"]:
                if action["agent_id"] == agent_id:
                    action["type"] = action_type
                    action["dx"] = dx
                    action["dy"] = dy
        else:
            actions["actions"].append({
                "team_id": team_id,
                "agent_id": agent_id,
                "type": action_type,
                "dx": dx,
                "dy": dy,
                "turn": turn,
                "apply": -1
            })
        manager.update(battle_id, turn, json.dumps(actions))
