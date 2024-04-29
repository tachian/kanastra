import logging
import os

from dotenv import load_dotenv
from json import loads

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):

    DEBUG = False
    TESTING = False
    DEPLOY_ENV = os.environ.get("DEPLOY_ENV", "Development")
    LOGS_LEVEL = logging.INFO

    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', "sqlite:///{}".format(os.path.join(basedir, 'database.db')))
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FILE_UPLOADS = os.environ.get('FILE_UPLOADS', f'{os.path.join(basedir)}/files')
    
    SEND_SLIPS_CRON_PARAMS = loads(os.environ.get('SEND_SLIPS_CRON_PARAMS', '{"minute":"*/1"}'))
    # '{"hour":"8"}'
    
class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', "sqlite:///{}".format(os.path.join(basedir, 'database-teste.db')))

class StagingConfig(BaseConfig):
    pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    LOGS_LEVEL = int(os.environ.get("LOG_LEVEL",logging.INFO))
