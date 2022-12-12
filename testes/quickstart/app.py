from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

#app = Flask(__name__)

'''
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
'''
'''
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


'''
'''
@app.route('/login')
def login():
    return 'login'


#Verificar URL Build
with app.test_request_context():
    print(url_for('hello', name='Bob'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''

'''


with app.test_request_context():
    url_for('static', filename='style1.css')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login'
    else:
        return 'show_the_login_form 1'


@app.get('/login')
def login_get():
    return 'show_the_login_form'

@app.post('/login')
def login_post():
    return 'do_the_login'


'''
#url_for('static', filename='style1.css')
'''

@app.route('/template/')
def template(name="<hr>hacker"):
    return render_template('hello.html', name=name)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


#with app.request_context(environ):
#    assert request.method == 'POST'

@app.route('/variavel')
def variavel(name="<hr>hacker"):
    searchword = request.args.get('key', '')
    return render_template('hello.html', name=searchword)



UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''

'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
'''
'''

from flask import make_response

@app.route('/')
def index():
    username = request.cookies.set('username')
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

'''
'''
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
'''

'''
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
'''
'''
from flask import make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

'''
'''
app = Flask(__name__)

@app.route("/me")
def me_api():
    user = { "username": "Derreck", "theme": "azul"}
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
    return {
        "username": user["username"],
        "theme": user["theme"],
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
'''


'''
from flask import session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return ''''''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    ''''''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
'''

'''
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
            app.logger.error('An error occurred')
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
'''


#The Application Factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
    






