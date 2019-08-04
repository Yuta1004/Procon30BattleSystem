from flask import Blueprint, jsonify, request
from server import base_route
from server.db.battle_db_manager import BattleDBAccessManager
from server.battle.register import battle_register as battle_register_func

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
    battle_id = int(battle_id)
    battle_list = BattleDBAccessManager().get_data(battle_id=battle_id)
    if len(battle_list) == 0:
        return jsonify(status="InvalidBattleID"), 401

    # 一部キー名を変更する
    battle = battle_list[0]
    battle["battleID"] = battle.pop("id")
    battle["startAtUnixTime"] = battle.pop("start_at_unix_time")
    battle["turnMillis"] = battle.pop("turn_mills")
    battle["intervalMillis"] = battle.pop("interval_mills")
    battle.pop("now_battle")

    return jsonify(battle_list[0]), 200


@route_battle.route(base_route + "/battle/register", methods=["POST"])
def battle_register():
    req_json = request.json
    battle_id = battle_register_func(
        req_json["name"],               # 試合名
        req_json["startAtUnixTime"],    # 試合開始時刻
        req_json["turn"],               # ターン数
        req_json["width"],              # 盤面サイズ(幅)
        req_json["height"],             # 盤面サイズ(縦)
        req_json["pointLower"],         # 配置得点(下限)
        req_json["pointUpper"],         # 配置得点(上限)
        req_json["playerNum"],          # プレイヤー数(1チーム)
        req_json["teamA"],              # チームAのID
        req_json["teamB"],              # チームBのID
        req_json["generateBoardType"],  # 生成する盤面のタイプ(0~2)
        req_json["turnMillis"],         # 1ターンの秒数
        req_json["intervalMillis"]      # ターン切り替えの秒数
    )

    return jsonify(battleID=battle_id), 200
