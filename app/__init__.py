from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '348032348643'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/employee.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key="True")
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    position = db.Column(db.String(30))
    location = db.Column(db.String(30))
    startdate = db.Column(db.Date)
    duration = db.Column(db.Integer)
    enddate = db.Column(db.Date)
    vacationEnt = db.Column(db.Integer)
    vacationtaken = db.Column(db.Integer)
    vacationBalance = db.Column(db.Integer)
    sickLeaveTaken = db.Column(db.Integer)
    sickLeaveBalance = db.Column(db.Integer)
    leaveNoPay = db.Column(db.Integer)
    salary = db.Column(db.Float)
    retention = db.Column(db.Float)
    netBasicSalary = db.Column(db.Float)
    score = db.Column(db.Integer)

db.create_all()

from app import views