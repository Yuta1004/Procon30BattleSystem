from flask import Blueprint
from server import base_route

route_top = Blueprint(__name__, "top")


@route_top.route(base_route + "/")
def top():
    return "#procon30 Battle API"
