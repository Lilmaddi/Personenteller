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

app.config['SECRET_KEY'] = 'mijngeheimesleutel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Macbook/OneDrive/Documenten/School/ICT/P3/IOT/code/Personenteller/env/lib/python3.8/site-packages/sqlalchemy/dialects/sqlite/'
db = SQLAlchemy(app)

class InfoForm(FlaskForm):

     username = StringField('E-mailadres', validators=[InputRequired()])
     password = PasswordField('Wachtwoord', validators=[InputRequired(),Length(min=8,max=80)])
     usercheck = BooleanField('Ingelogd blijven')
     submit = SubmitField('submit')

@app.route("/", methods=['GET', 'POST'])
def login():
    form = InfoForm()

    # if form.validate_on_submit():
    #     return render_template("home.html",form=form)

    return render_template("login.html",form=form) 

@app.route("/home/")
def home():
    return render_template("home.html")  

if __name__ == "__main__":
    app.run(debug=True)