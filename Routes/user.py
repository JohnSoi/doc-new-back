from flask import request
from flask_cors import cross_origin
from app import app, engine

from Class.User import User


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    request_data = request.get_json() or {}
    return User.login(engine.session, request_data.get('login'), request_data.get('password'))


@app.route('/user/list', methods=['POST'])
@cross_origin()
def get():
    request_data = request.get_json() or {}
    return User.list(engine.session, request_data.get('navigation'), request_data.get('filter'))


@app.route('/user/create', methods=['POST'])
@cross_origin()
def create_user():
    request_data = request.get_json() or {}
    return User.create(request_data)


@app.route('/user/update', methods=['POST'])
@cross_origin()
def update_user():
    request_data = request.get_json() or {}
    return User.update(request_data)


@app.route('/user/search', methods=['POST'])
@cross_origin()
def search_user():
    request_data = request.get_json() or {}
    return User.search(engine.session, request_data.get('searchString'))