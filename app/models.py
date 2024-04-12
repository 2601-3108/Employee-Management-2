# model.py
from flask_sqlalchemy import SQLAlchemy
from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False, index=True)
    lastname = db.Column(db.String(50), nullable=False, index=True)
    phonenumber = db.Column(db.String(20), unique=True, nullable=False, index=True)  # Ensure uniqueness
    gender = db.Column(db.String(10), nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)  # Ensure uniqueness


    def __repr__(self):
        return f'<Employee {self.firstname + " " + self.lastname}>'
 