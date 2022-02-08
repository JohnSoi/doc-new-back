from Class.System import System
from .permission import *
from .user import *
from .role import *
from .patient import *
from .service import *


@app.route('/default-settings', methods=['GET'])
@cross_origin()
def set_default_data():
    return System.add_default_data()
