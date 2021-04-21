from personenteller import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, login_required, logout_user

class Type(db.Model):

    __tablename__ = 'type'

    id = db.Column(db.Integer,primary_key = True) #type bungalow
    pers = db.Column(db.Integer)
    prijs = db.Column(db.Integer)

    def __init__(self,pers,prijs):
        self.pers = aantalpersonen
        self.prijs = weekprijs

class Accomodatie(db.Model):

    __tablename__ = 'accomodatie'

    id = db.Column(db.Integer,primary_key = True) #type bungalow
    naam = db.Column(db.Text)
    type = db.Column(db.Integer,db.ForeignKey('type.id'))

    def __init__(self,pers,prijs):
        self.naam = naam
        self.type = type

@login_manager.user_loader
def load_user(klant_id):
    return Klant.query.get(klant_id)


class Klant(db.Model, UserMixin):

    __tablename__ = 'klanten'

    id = db.Column(db.Integer,primary_key = True)
    voornaam = db.Column(db.String(64))
    achternaam = db.Column(db.String(64))
    emailadres = db.Column(db.String(64), unique=True, index=True)
    wachtwoord_hash = db.Column(db.String(128))

    def __init__(self,voornaam,achternaam,emailadres,wachtwoord):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.emailadres = emailadres
        self.wachtwoord_hash = generate_password_hash(wachtwoord)

    def check_password(self, wachtwoord):
        return check_password_hash(self.wachtwoord_hash, wachtwoord)

class Medewerker(db.Model):

    __tablename__ = 'medewerker'

    id = db.Column(db.Integer,primary_key = True)
    naam = db.Column(db.Text)

    def __init__(self,naam):
        self.naam = naam

class Reservering(db.Model, UserMixin):

    __tablename__ = 'reserveringen'

    id = db.Column(db.Integer,primary_key = True)
    klantid = db.Column(db.Integer,db.ForeignKey('klanten.id')) 
    typebungalow = db.Column(db.Integer,db.ForeignKey('accomodatie.id'))
    weeknummer = db.Column(db.Text)

    def __init__(self,klantid,typebungalow,weeknummer):
        self.klantid = klantid
        self.typebungalow = typebungalow
        self.weeknummer = weeknummer
    
    def __repr__(self):
        return f"{self.id} | U heeft een reservering voor {self.typebungalow} personen in weeknummer {self.weeknummer}."

db.create_all()


