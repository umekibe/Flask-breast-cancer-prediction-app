from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Patient_data(db.Model):
    Patient_id = db.Column(db.Integer, primary_key=True)
    P_name = db.Column(db.String(150), unique=True)
    diagnosis_results = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Patient_data('{self.P_name}', '{self.diagnosis_results}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(150), unique=True)
    password= db.Column(db.String(150))
    first_name= db.Column(db.String(150))
    Patient_data = db.relationship('Patient_data')

    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}')"

