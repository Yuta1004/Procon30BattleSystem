from flask import Flask

# Config
base_route = "/procon30-battle-api"

# APP Setup
app = Flask(__name__)

# Blueprint
from server.views.top import route_top
from server.views.battle_api import route_battle
from server.views.match_api import route_match
from server.views.ping_api import route_ping

app.register_blueprint(route_top)
app.register_blueprint(route_battle)
app.register_blueprint(route_match)
app.register_blueprint(route_ping)
