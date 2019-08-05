from flask import Blueprint, jsonify, request
from server import base_route
from server.db.team_db_manager import TeamDBAccessManager

route_team = Blueprint(__name__, "team")


@route_team.route(base_route + "/team")
def team_top():
    team_db_manager = TeamDBAccessManager()
    team_list = team_db_manager.get_data()
    return jsonify(team_list), 200
