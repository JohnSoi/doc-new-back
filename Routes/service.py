from flask import request
from flask_cors import cross_origin
from app import app, engine

from Class.Service import Service


@app.route('/service/list', methods=['POST'])
@cross_origin()
def get_service():
    request_data = request.get_json() or {}
    return Service.list(engine.session, request_data.get('navigation'), request_data.get('filter'))


@app.route('/service/create', methods=['POST'])
@cross_origin()
def create_service():
    request_data = request.get_json() or {}
    return Service.create(request_data)


@app.route('/service/update', methods=['POST'])
@cross_origin()
def update_service():
    request_data = request.get_json() or {}
    return Service.update(request_data)
