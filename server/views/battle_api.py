from flask import Blueprint, jsonify
from server import base_route
from server.db.battle_db_manager import BattleDBAccessManager

route_battle = Blueprint(__name__, "battle")


@route_battle.route(base_route + "/battle")
def battle_top():
    battle_list = BattleDBAccessManager().get_data()
    battle_list = list(filter(lambda x: x["now_battle"] == 1, battle_list))

    # 一部キー名を変更する
    for battle in battle_list:
        battle["battleID"] = battle.pop("id")
        battle["startAtUnixTime"] = battle.pop("start_at_unix_time")
        battle["turnMillis"] = battle.pop("turn_mills")
        battle["intervalMillis"] = battle.pop("interval_mills")
        battle.pop("now_battle")

    return jsonify(battle_list), 200


@route_battle.route(base_route + "/battle/<battle_id>")
def battle_view(battle_id):
    battle_list = BattleDBAccessManager().get_data(battle_id=battle_id)
    if battle_list is None:
        return jsonify(status="InvalidBattleID"), 401

    # 一部キー名を変更する
    battle = battle_list[0]
    battle["battleID"] = battle.pop("id")
    battle["startAtUnixTime"] = battle.pop("start_at_unix_time")
    battle["turnMillis"] = battle.pop("turn_mills")
    battle["intervalMillis"] = battle.pop("interval_mills")
    battle.pop("now_battle")

    return jsonify(battle_list[0]), 200


@route_battle.route(base_route + "/battle/register")
def battle_register():
    return "Register Battle"
