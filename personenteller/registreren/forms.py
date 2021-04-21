from personenteller.models import *
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired
from wtforms import (IntegerField, StringField, SelectField,
                    PasswordField, 
                    BooleanField,  
                    SubmitField)

class RegistrationForm(FlaskForm):
     voornaam = StringField('Voornaam', validators=[InputRequired()])
     achternaam = StringField('Achternaam', validators=[InputRequired()])
     email = StringField('Email Address', validators=[InputRequired(),Email()])
     wachtwoord = PasswordField('Wachtwoord', validators=[InputRequired()]) # EqualTo('Bevestigen', message='Bovenstaande twee wachtwoorden moeten aan elkaar gelijk zijn.')]
     confirm = PasswordField('Herhaal wachtwoord')
     usercheck = BooleanField('Ingelogd blijven')
     submit = SubmitField('Registreren')

     