from flask import Flask

from processos.ext import config



def create_app():
    app = Flask(__name__)
    config.init_app(app)
    return app





'''
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'processos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
'''
# ...




'''
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
'''