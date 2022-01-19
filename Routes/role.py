from flask import request
from flask_cors import cross_origin
from app import app, engine

from Class.Role import Role


@app.route('/role/list', methods=['POST'])
@cross_origin()
def get_role():
    request_data = request.get_json() or {}
    return Role.list(engine.session, request_data.get('navigation'), request_data.get('filter'))