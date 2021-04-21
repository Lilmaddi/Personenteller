import os

from personenteller import app, db,login_manager
from personenteller.models import *
from personenteller.login.views import *
from personenteller.login.forms import LoginForm

from flask import Flask, render_template, session, redirect, url_for, session, flash,request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


login_blueprint = Blueprint('login', __name__, template_folder='templates')

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
        user = Klant.query.filter_by(emailadres=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
        
        if user is not None and user.check_password(form.wachtwoord.data):
            
            login_user(user) # Log in the user
            flash('U bent succesvol ingelogd.')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('home')
            
            return redirect(next)

        else:
            flash('De combinatie van het wachtwoord en het gebruikersnaam is incorrect.')

    return render_template('login.html',form=form)

@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('U bent uitgelogd')
    return redirect(url_for('home')) 


