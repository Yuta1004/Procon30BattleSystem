from flask import Flask

# Config
base_route = "/megurimasuapi"

# APP Setup
app = Flask(__name__)

# Blueprint
from server.views.top import route_top

app.register_blueprint(route_top)
