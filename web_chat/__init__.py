from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from web_chat import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
db=SQLAlchemy(app)
login_manager=LoginManager(app)
app.secret_key=config.SECRET_KEY

from web_chat import routes, models
