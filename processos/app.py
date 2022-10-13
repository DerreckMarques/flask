from processos.ext import rotas
from flask import Flask

app = Flask(__name__)


rotas.init_app(app)



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