from flask import Blueprint, Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .config import Config

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)
db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


def create_app():
    from . import resource

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)
    app.register_blueprint(apiv1_bp)
    return app
