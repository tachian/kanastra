import logging
import os
import sys

import json_logging
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sqlalchemy import MetaData

ENV = os.environ.get('DEPLOY_ENV', 'Development')

convention = {
    "ix": "ix_%(column_0_label)s",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
    "uq": "%(table_name)s_%(column_0_name)s_key"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

csrf = CSRFProtect()
def create_app(deploy_env: str = ENV) -> Flask:
    app = Flask(__name__)

    csrf.init_app(app)

    CORS(app)
    app.config.from_object('src.config.{}Config'.format(deploy_env))

    __register_blueprints_and_error_handling(app)
    __configure_logger(app)

    db.init_app(app)
    Migrate(app, db)

    return app

def __register_blueprints_and_error_handling(app: Flask):
    from src.presentation_layer.views.api import bp_index

    app.register_blueprint(bp_index)
    csrf.exempt(bp_index)


def __configure_logger(app: Flask):
    if not json_logging.ENABLE_JSON_LOGGING:
        json_logging.init_flask(enable_json=True)
        json_logging.init_request_instrument(app)

    logger = logging.getLogger("kanastra")
    logger.setLevel(app.config["LOGS_LEVEL"])
    logger.addHandler(logging.StreamHandler(sys.stdout))



