from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from Config.common import PRODUCTION
from Platform.Database.connect import EngineConnect

app = Flask(__name__)
app.config.from_object('Config.common')
CORS(app)
engine = EngineConnect()
db = SQLAlchemy(app)
BaseModel = db.Model
migrate = Migrate(app, db)

from Routes.user import *

if __name__ == '__main__':
    app.run(debug=not PRODUCTION)