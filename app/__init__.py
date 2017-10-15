from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '348032348643'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/employee.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class employee(db.Model):
    id = db.Column(db.Integer, primary_key="True")
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    position = db.Column(db.String(30))
    location = db.Column(db.String(30))
    startdate = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    enddate = db.Column(db.DateTime)
    vacationEnt = db.Column(db.Integer,default=10)
    vacationtaken = db.Column(db.Integer,default=0)
    vacationBalance = db.Column(db.Integer,default=10)
    sickLeaveTaken = db.Column(db.Integer, default=0)
    sickLeaveBalance = db.Column(db.Integer, default=0)
    leaveNoPay = db.Column(db.Integer,default =0)
    salary = db.Column(db.Float)
    retention = db.Column(db.Float)
    netBasicSalary = db.Column(db.Float)
    score = db.Column(db.Integer, default =0)

db.create_all()

from app import views