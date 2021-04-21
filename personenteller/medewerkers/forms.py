from personenteller.models import *
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired
from wtforms import (IntegerField, StringField, SelectField,
                    PasswordField, 
                    BooleanField,  
                    SubmitField)


class AddForm(FlaskForm):
    naam = StringField('Naam medewerker:')
    submit = SubmitField('Voeg toe')

class DelForm(FlaskForm):
    id = SelectField('Verwijder een medewerker uit het systeem:')
    submit = SubmitField('Verwijderen')

#class UpdateForm(FlaskForm):
