from flask import request
from flask_cors import cross_origin
from app import app, engine

from Class.Operation import Operation


@app.route('/operation/list', methods=['POST'])
@cross_origin()
def get_operation():
    request_data = request.get_json() or {}
    return Operation.list(engine.session, request_data.get('navigation'), request_data.get('filter'))


@app.route('/operation/create', methods=['POST'])
@cross_origin()
def create_operation():
    request_data = request.get_json() or {}
    return Operation.create(request_data)


@app.route('/operation/update', methods=['POST'])
@cross_origin()
def update_operation():
    request_data = request.get_json() or {}
    return Operation.update(request_data)
