from flask import Blueprint, request, jsonify
from server import base_route
from server.api_func.matches import get_all_matches, get_match_detail
from server.api_func.action_send import action_send

route_match = Blueprint(__name__, "match-api")


@route_match.route(base_route + "/matches", methods=["GET"])
def matches_top():
    token = request.headers.get("Authorization")
    status, match_list = get_all_matches(token)
    return jsonify(match_list), status


@route_match.route(base_route + "/matches/<battle_id>")
def matches_details(battle_id):
    battle_id = int(battle_id)
    token = request.headers.get("Authorization")
    status, match_detail = get_match_detail(token, battle_id)
    return jsonify(match_detail), status


@route_match.route(base_route + "/matches/<battle_id>/action", methods=["POST"])
def matches_receive_action(battle_id):
    battle_id = int(battle_id)
    if request.headers.get("Content-Type") != "application/json":   # 一応確認
        return "Must set the header \"Content-Type:application/json\"", 400
    token = request.headers.get("Authorization")
    action_data = request.json
    status, response = action_send(token, battle_id, action_data)
    return jsonify(response), status
