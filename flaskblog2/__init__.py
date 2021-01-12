from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/flaskblog2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'fb1a97349eaa6286b0d65b08bcdf6917'

from flaskblog2 import routes