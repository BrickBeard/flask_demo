from flask_migrate import Migrate
from project import app
from project.models import db


# Database Management  ('flask db migrate' & 'flask db upgrade')
migrate = Migrate(app, db)