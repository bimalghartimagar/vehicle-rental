from flask_restful import Resource
from flask import request

from rentalapi.dao.models import Users
from rentalapi.schema import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UsersAPI(Resource):
    def get(self):
        users = Users.query.all()

        return users_schema.dump(users).data


class UserAPI(Resource):
    def get(self, user_id):
        user = Users.query.filter_by(id=user_id).first()

        if not user:
            abort(
                404,
                message="user id {} doesn't exist".format(user_id))

        return user_schema.dump(user).data

    def post(self):
        data = request.get_json()

        user, errors = user_schema.load(data)

        if errors:
            abort(422, message=errors)

        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.sessoion.rollback()

        return user_schema.dump(user).data

    def put(self, user_id):
        user = Users.query.get(user_id)

        if not user:
            abort(
                404,
                message="user id {} doesn't exist".format(user_id))

        data = request.json()
        put_user, errors = user_schema.load(data)

        if errors:
            abort(422, message=errors)

        user.name = put_user.name

        try:
            db.session.commit()
        except:
            db.session.rollback()

        return user_schema.dump(user).data

    def delete(self, user_ud):
        user = Users.query.get(user_id)

        if not user:
            abort(
                404,
                message="user id {} doesn't exist".format(user_ud)
                )

        try:
            db.session.delete(user)
            db.session.commit()
        except:
            db.session.rollback()

        return user_schema.dump(user).data
