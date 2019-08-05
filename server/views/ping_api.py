from flask import Blueprint, jsonify, request
from server import base_route
from server.api_func.check import token_check

route_ping = Blueprint(__name__, "ping")


@route_ping.route(base_route + "/ping")
def ping():
    token = request.headers.get("Authorization")
    is_error, status, response = token_check(token)
    if is_error:
        return jsonify(response), status
    else:
        return jsonify(status="OK"), 200
