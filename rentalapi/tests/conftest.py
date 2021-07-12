import pytest
from rentalapi.app import create_app
from rentalapi.dao.models import Users, UserTypes, db


@pytest.fixture(scope='module')
def new_test_user():
    user = Users('test@test.com', 'test_username', 'test_password')
    return user


@pytest.fixture(scope='module')
def test_client():
    app = create_app('dev.cfg')

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


@pytest.fixture(scope='module')
def test_client_with_db():
    app = create_app('dev.cfg')

    with app.test_client() as test_client:
        with app.app_context():
            db.drop_all()
            db.create_all()

            admin_type = UserTypes(name='ADMIN')
            db.session.add(admin_type)
            db.session.commit()

            admin = Users('admin@admin.com', 'admin',
                          'admin123', admin_type.id)
            db.session.add(admin)
            db.session.commit()

            yield test_client


@pytest.fixture(scope='module')
def resources():
    return ['rentals', 'users', 'usertypes', 'vehicles', 'vendors']


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username, password):
        return self._client.post(
            '/api/auth/login/',
            json={
                'username': username,
                'password': password
            }
        )

    def logout(self, token):
        return self._client.delete('/api/auth/logout/')


@pytest.fixture(scope='module')
def auth(test_client_with_db):
    return AuthActions(test_client_with_db)
