from Platform.app_platform import app, engine, BaseModel

from Config.common import PRODUCTION

app.config.from_object('Config.common')

from Routes import *

if __name__ == '__main__':
    app.run(debug=not PRODUCTION)
