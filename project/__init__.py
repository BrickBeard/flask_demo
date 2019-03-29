from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('dev.cfg')
CORS(app)

db = SQLAlchemy(app)

from project import views