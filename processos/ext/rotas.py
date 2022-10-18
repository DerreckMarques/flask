from flask import Blueprint, render_template


example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/index')
@example_blueprint.route('/')
def index():
    return render_template("index.html")

def init_app(app):
    app.register_blueprint(example_blueprint)