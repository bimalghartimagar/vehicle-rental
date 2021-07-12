from functools import wraps
from flask_jwt_extended import (get_jwt_identity, verify_jwt_in_request)
from rentalapi.dao.models import Users


def role_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()

        identity = get_jwt_identity()
        user = identity.split(':')
        current_user = Users.query.filter_by(
            username=user[0], id=user[1]).first()
        if not current_user:
            return {'msg': 'Invalid Request'}, 400

        if current_user.usertype.name == 'ADMIN':
            return fn(*args, **kwargs)
        else:
            return {'msg': 'Not Authorized'}, 403

    return wrapper
