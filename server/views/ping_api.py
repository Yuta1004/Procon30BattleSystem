from flask import Blueprint, jsonify
from server import base_route

route_ping = Blueprint(__name__, "ping")


@route_ping.route(base_route + "/ping")
def ping():
    return jsonify(status="OK")
