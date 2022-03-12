from Class.Search import Search
from Class.Statistics import Statistic
from Class.System import System
from .permission import *
from .user import *
from .role import *
from .patient import *
from .service import *
from .operation import *
from Platform.Routes import *


@app.route('/default-settings', methods=['GET'])
@cross_origin()
def set_default_data():
    return System.add_default_data()


@app.route('/universal_search/get', methods=['POST'])
@cross_origin()
def univeral_search():
    request_data = request.get_json() or {}
    return Search.universal_search(engine.session, request_data.get('searchString'), request_data.get('type'))


@app.route('/statistics/patients', methods=['POST'])
@cross_origin()
def patient_statistic():
    request_data = request.get_json() or {}
    return Statistic().patient(request_data.get('filter'))
