from flask import Flask
from dynaconf import FlaskDynaconf

app = Flask(__name__)
flask_dynaconf = FlaskDynaconf(app)

print(app.config.TESTE)
