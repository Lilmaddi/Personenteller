from personenteller.models import *
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired
from wtforms import (IntegerField, StringField, SelectField,
                    PasswordField, 
                    BooleanField,  
                    SubmitField)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    wachtwoord = PasswordField('Password', validators=[InputRequired()])
    usercheck = BooleanField('Ingelogd blijven')
    submit = SubmitField('Log In')