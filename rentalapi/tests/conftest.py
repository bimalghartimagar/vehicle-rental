import pytest
from rentalapi.app import create_app
from rentalapi.dao.models import Users


@pytest.fixture(scope='module')
def new_test_user():
    user = Users('test@test.com', 'test_username', 'test_password')
    return user

@pytest.fixture(scope='module')
def test_client():
  app = create_app('test.cfg')

  with app.test_client() as test_client:
    with app.app_context():
      yield test_client