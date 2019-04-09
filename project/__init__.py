from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .models import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('dev.cfg')
    CORS(app)

    db.init_app(app)

    from .portal.views import portal_bp
    from .api.views import api_bp
    from .api.v1.routes import v1
    from .api.v2.routes import v2

    app.register_blueprint(portal_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(v1, url_prefix='/api/v1')
    app.register_blueprint(v2, url_prefix='/api/v2')

    return app

app = create_app()