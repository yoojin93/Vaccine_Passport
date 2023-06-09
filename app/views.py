from app import app
import app.db.doctor_db as doctor_db
from flask import render_template, request

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/patients", methods=["POST"])
def list_of_patients():
    doctor_db.register_doctor(request.form)
    return "Form submitted"

@app.route("/patient")
def individual_patient():
    return "Individual patient"