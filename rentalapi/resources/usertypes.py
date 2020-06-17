from flask_restful import Resource, abort
from flask import current_app, request

from rentalapi.schema import UserTypeSchema
from rentalapi.dao.models import UserTypes as UserTypesModel
from rentalapi.dao.models import db

user_type_schema = UserTypeSchema()
user_types_schema = UserTypeSchema(many=True)


class UserTypesAPI(Resource):
    def get(self):
        user_types = UserTypesModel.query.all()

        return user_types_schema.dump(user_types)

    def post(self):
        current_app.logger.debug("IN POst")
        data = request.get_json()
        current_app.logger.debug(data)
        current_app.logger.debug(dir(user_type_schema))
        current_app.logger.debug(user_type_schema.fields)
        # user_type, errors = user_type_schema.load(data)
        user_type = UserTypesModel(name=data["name"])
        errors = None
        if errors:
            abort(422, message=errors)

        try:
            db.session.add(user_type)
            db.session.commit()
        except:
            db.session.rollback()

        return user_type_schema.dump(user_type)


class UserTypeAPI(Resource):
    def get(self, user_type_id):
        user_type = UserTypesModel.query.filter_by(id=user_type_id).first()

        if not user_type:
            abort(
                404,
                message="User Type id {} doesn't exist".format(user_type_id)
                )

        return user_type_schema.dump(user_type)

    def put(self, user_type_id):

        user_type = UserTypesModel.query.get(user_type_id)

        if not user_type:
            abort(
                404,
                message="User Type id {} doesn't exist".format(user_type_id)
                )

        data = request.get_json()
        put_user_type, errors = user_type_schema.load(data)

        if errors:
            abort(422, message=errors)

        user_type.name = put_user_type.name

        try:
            db.session.commit()
        except:
            db.session.rollback()

        return user_type_schema.dump(user_type)

    def delete(self, user_type_id):
        user_type = UserTypesModel.query.get(user_type_id)

        if not user_type:
            abort(
                404,
                message="User Type id {} doesn't exist".format(user_type_id)
                )

        try:
            db.session.delete(user_type)
            db.session.commit()
        except:
            db.session.rollback()

        return user_type_schema.dump(user_type)
