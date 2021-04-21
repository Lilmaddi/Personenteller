from flask import Blueprint, render_template, redirect, url_for
from personenteller import db, app
from personenteller.medewerkers.forms import AddForm, DelForm
from personenteller.models import *


medewerkers_blueprint = Blueprint('medewerkers', __name__, template_folder='templates')

@medewerkers_blueprint.route('/medewerkers', methods=['GET', 'POST'])
def medewerkers():

    form = AddForm()
    form2 = DelForm()

    if form.validate_on_submit() and form.naam.data != "":
        naam = form.naam.data
        new_medewerker = Medewerker(naam)
        db.session.add(new_medewerker)
        db.session.commit()
        
    form2.id.choices = [(medewerker.id, medewerker.naam) for medewerker in Medewerker.query.order_by('naam')]

    if form2.validate_on_submit():
        id = form2.id.data
        medewerker = Medewerker.query.get(id)
        db.session.delete(medewerker)
        db.session.commit()
    
    medewerker = Medewerker.query.all()

    return render_template('overzichtmed.html',form=form, form2=form2, Medewerker=medewerker) 