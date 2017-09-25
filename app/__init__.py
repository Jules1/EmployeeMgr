from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '348032348643'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////employee.db'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

from app import views