from flask_migrate import Migrate
from project import app
from project.models import User, Company, db


# Database Management  ('flask db migrate' & 'flask db upgrade')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Company=Company)