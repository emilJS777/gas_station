from flask import Flask, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import datetime
import logging
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_mail import Mail

app = Flask(__name__)
api = Api(app)

# CONNECT TO DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<password>@localhost/gas_station_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
migrate = Migrate(app, db)

# IMAGE
app.config["IMAGE_UPLOADS"] = 'files/images'

# CONNECT JWT CONFIG
app.config["JWT_SECRET_KEY"] = "H^&67KCsn@77G"
app.config["JWT_ACCESS_EXP"] = 60*24
app.config["JWT_REFRESH_EXP"] = 3000
jwt = JWTManager(app)

# Set CORS options on app configuration
app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, supports_credentials=True)

# LOGGING
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(f"{datetime.utcnow()}")

socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*")

# MAIL CONFIG
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'test-test-9292@mail.ru'
app.config['MAIL_PASSWORD'] = 'i5H8SqqL9fHmLxyLsKBU'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
