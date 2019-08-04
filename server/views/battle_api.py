from flask import Blueprint
from server import base_route

route_battle = Blueprint(__name__, "battle")


@route_battle.route(base_route + "/battle")
def battle_top():
    return "View Battle List"


@route_battle.route(base_route + "/battle/{battle_id}")
def battle_view(battle_id):
    return "View Battle : " + battle_id


@route_battle.route(base_route + "/battle/register")
def battle_register():
    return "Register Battle"
