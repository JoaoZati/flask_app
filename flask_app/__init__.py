from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)  # converter para SQL
migrate = Migrate(app, db)

from flask_app.models import tables, forms
from flask_app.controllers import default
