from flask import Blueprint, render_template
from processos.ext.db.models import Processo


example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/index')
@example_blueprint.route('/')
def index():
    processos = Processo.query.all()
    return render_template('index.html', processos=processos)

def init_app(app):
    app.register_blueprint(example_blueprint)