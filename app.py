import os
from personenteller import app, db,login_manager

from personenteller.login.views import login_blueprint
from personenteller.medewerkers.views import medewerkers_blueprint
from personenteller.registreren.views import registreren_blueprint

from flask_migrate import Migrate
from flask import Flask, render_template, session, redirect, url_for, session, flash,request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap

Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    
    app.run(debug=True)