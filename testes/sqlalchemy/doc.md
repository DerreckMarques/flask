https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/

Installation
Flask-SQLAlchemy is available on PyPI and can be installed with various Python tools. For example, to install or update the latest version using pip:

$ pip3 install -U Flask-SQLAlchemy

Configure the Extension
The only required Flask app config is the SQLALCHEMY_DATABASE_URI key. That is a connection string that tells SQLAlchemy what database to connect to.

Create your Flask application object, load any config, and then initialize the SQLAlchemy extension class with the application by calling db.init_app. This example connects to a SQLite database, which is stored in the app’s instance folder.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testes.db"
# initialize the app with the extension
db.init_app(app)



Define Models
Subclass db.Model to define a model class. The db object makes the names in sqlalchemy and sqlalchemy.orm available for convenience, such as db.Column. The model will generate a table name by converting the CamelCase class name to snake_case.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

The table name "user" will automatically be assigned to the model’s table.

Create the Tables
After all models and tables are defined, call SQLAlchemy.create_all() to create the table schema in the database. This requires an application context. Since you’re not in a request at this point, create one manually.

with app.app_context():
    db.create_all()

If you define models in other modules, you must import them before calling create_all, otherwise SQLAlchemy will not know about them.

create_all does not update tables if they are already in the database. If you change a model’s columns, use a migration library like Alembic with Flask-Alembic or Flask-Migrate to generate migrations that update the database schema.


Query the Data
Within a Flask view or CLI command, you can use db.session to execute queries and modify model data.

SQLAlchemy automatically defines an __init__ method for each model that assigns any keyword arguments to corresponding database columns and other attributes.

db.session.add(obj) adds an object to the session, to be inserted. Modifying an object’s attributes updates the object. db.session.delete(obj) deletes an object. Remember to call db.session.commit() after modifying, adding, or deleting any data.

db.session.execute(db.select(...)) constructs a query to select data from the database. Building queries is the main feature of SQLAlchemy, so you’ll want to read its tutorial on select to learn all about it. You’ll usually use the Result.scalars() method to get a list of results, or the Result.scalar() method to get a single result.

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("user/list.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")

@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("user/delete.html", user=user)

You may see uses of Model.query to build queries. This is an older interface for queries that is considered legacy in SQLAlchemy. Prefer using db.session.execute(db.select(...)) instead.
