from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views
from app import models

app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = '571ebf8e12ca209536c'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///doctor_patient_information.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config.from_object('config')

