from flask import request
from flask_cors import cross_origin
from app import app, engine

from Class.Permission import Permission


@app.route('/permission/list', methods=['POST'])
@cross_origin()
def get_permission():
    request_data = request.get_json() or {}
    return Permission.list(engine.session, request_data.get('navigation'), request_data.get('filter'))