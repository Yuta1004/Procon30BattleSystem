from flask import Blueprint, request, jsonify
from server import base_route
from server.api_func.matches import get_all_matches

route_match = Blueprint(__name__, "match-api")


@route_match.route(base_route + "/matches", methods=["GET"])
def matches_top():
    token = request.headers.get("Authorization")
    match_list = get_all_matches(token)
    return jsonify(match_list)


@route_match.route(base_route + "/matches/<battle_id>")
def matches_details(battle_id):
    return "Return Battle Info : " + battle_id


@route_match.route(base_route + "/matches/<battle_id>/action", methods=["POST"])
def matches_receive_action(battle_id):
    return "Received Action Data : " + battle_id
