from .main import example_blueprint


def init_app(app):
    app.register_blueprint(example_blueprint)