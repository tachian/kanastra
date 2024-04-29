import os
import pytest

from src.app import create_app, db

        
@pytest.fixture(scope='function')
def app():
    os.environ["DEPLOY_ENV"] = "Testing"
    app = create_app('Testing')
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        db.metadata.bind = db.engine
        db.create_all()
        yield client
        db.session.rollback()