from flask import Blueprint
from server import base_route

route_match = Blueprint(__name__, "match-api")


@route_match.route(base_route + "/matches")
def matches_top():
    return "Return Match List(GET)"


@route_match.route(base_route + "/matches/<battle_id>")
def matches_details(battle_id):
    return "Return Battle Info : " + battle_id


@route_match.route(base_route + "/matches/<battle_id>/action", methods=["POST"])
def matches_receive_action(battle_id):
    return "Received Action Data : " + battle_id
