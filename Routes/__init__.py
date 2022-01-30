from Class.System import System
from .permission import *
from .user import *
from .role import *


@app.route('/default-settings', methods=['GET'])
@cross_origin()
def set_default_data():
    return System.add_default_data()