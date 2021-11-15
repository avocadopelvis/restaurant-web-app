from restaurant import db

#USER DATABASE
class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    email_address = db.Column(db.String(length = 50), nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 60), nullable = False) 

#TABLE RESERVATION DATABASE
class Table(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    table = db.Column(db.Integer(), nullable = False)
    time = db.Column(db.String(length = 20), nullable = False)
    date = db.Column(db.String(length = 20), nullable = False)
    accomodation = db.Column(db.Integer(), nullable = False)

#MENU DATABASE