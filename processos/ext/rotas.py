from flask import Blueprint


example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/')
def index():
    return "This is an example app"

def init_app(app):
    app.register_blueprint(example_blueprint)