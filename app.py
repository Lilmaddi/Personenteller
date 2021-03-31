import os
from flask import Flask, render_template, session, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email,Length
from wtforms import (StringField, 
                    PasswordField, 
                    BooleanField,  
                    SubmitField)

app = Flask(__name__)
Bootstrap(app)

# Geheime sleutel voor formulieren
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

# DB koppeling
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(basedir,'datasqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class InfoForm(FlaskForm):
     username = StringField('E-mailadres', validators=[InputRequired()])
     password = PasswordField('Wachtwoord', validators=[InputRequired(),Length(min=8,max=80)])
     usercheck = BooleanField('Ingelogd blijven')
     firstname = StringField('Voornaam', validators=[InputRequired()])
     lastname = StringField('Achternaam', validators=[InputRequired()])
     email = StringField('Email Address', validators=[InputRequired(),Email(),Length(min=6, max=35)])
     password1 = PasswordField('Wachtwoord', validators=[InputRequired()]) # EqualTo('Bevestigen', message='Bovenstaande twee wachtwoorden moeten aan elkaar gelijk zijn.')]
     confirm = PasswordField('Herhaal wachtwoord')
     submit = SubmitField('submit')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = InfoForm()

    # if form.validate_on_submit():
    #     return render_template("home.html",form=form)

    return render_template("login.html",form=form) 

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/registreren", methods=['GET', 'POST'])
def registreren():
    form = InfoForm()

    # if form.validate_on_submit():
    #     return render_template("home.html",form=form)

    return render_template("registreren.html",form=form)  

if __name__ == "__main__":
    app.run(debug=True)