from flask import Blueprint, render_template, redirect, url_for, flash
from personenteller import db, app
from personenteller.registreren.forms import RegistrationForm
from personenteller.models import *

registreren_blueprint = Blueprint('registreren', __name__, template_folder='templates')

@registreren_blueprint.route('/registreren', methods=['GET', 'POST'])
def registreren():
    
    form = RegistrationForm()

    if form.validate_on_submit():
        klant = Klant(voornaam=form.voornaam.data,
                    achternaam=form.achternaam.data,
                    emailadres = form.email.data,
                    wachtwoord = form.wachtwoord.data)

        if Klant.query.filter_by(emailadres = form.email.data).first():
            flash('Dit e-mailadres staat al geregistreerd!')
            redirect(url_for('registreren.registreren'))
        else:
            db.session.add(klant)
            db.session.commit()
            flash('Dank voor uw registratie. U kunt nu inloggen.')
            return redirect(url_for('home'))

        

    return render_template('registreren.html',form=form) 