import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)
Migrate(app,db)

# De app wordt bekend gemaakt bij de Loginmanager
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Hier wordt duideljk gemaakt welke view verantwoordelijk is voor het inloggen
login_manager.login_view = "login"

from personenteller.login.views import login_blueprint
from personenteller.medewerkers.views import medewerkers_blueprint
from personenteller.registreren.views import registreren_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(medewerkers_blueprint)
app.register_blueprint(registreren_blueprint)
