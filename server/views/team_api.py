from flask import Blueprint, jsonify, request
from server import base_route
from server.db.team_db_manager import TeamDBAccessManager

route_team = Blueprint(__name__, "team")


@route_team.route(base_route + "/team")
def team_top():
    team_db_manager = TeamDBAccessManager()
    team_list = team_db_manager.get_data()
    return jsonify(team_list), 200


@route_team.route(base_route + "/team/id/<team_id>")
def team_view_id(team_id):
    team_db_manager = TeamDBAccessManager()
    team = team_db_manager.get_data(team_id=team_id)
    if len(team) == 0:
        return jsonify(status="InvalidTeamID"), 400

    return jsonify(team[0]), 200


@route_team.route(base_route + "/team/token/<token>")
def team_view_token(token):
    team_db_manager = TeamDBAccessManager()
    team = team_db_manager.get_data(token=token)
    if len(team) == 0:
        return jsonify(status="InvalidToken"), 400

    return jsonify(team[0]), 200
