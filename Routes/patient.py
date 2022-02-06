from flask import request
from flask_cors import cross_origin
from app import app, engine

from Class.Patient import Patient


@app.route('/patient/list', methods=['POST'])
@cross_origin()
def get_patient():
    request_data = request.get_json() or {}
    return Patient.list(engine.session, request_data.get('navigation'), request_data.get('filter'))


@app.route('/patient/create', methods=['POST'])
@cross_origin()
def create_patient():
    request_data = request.get_json() or {}
    return Patient.create(request_data)


@app.route('/patient/update', methods=['POST'])
@cross_origin()
def update_patient():
    request_data = request.get_json() or {}
    return Patient.update(request_data)
