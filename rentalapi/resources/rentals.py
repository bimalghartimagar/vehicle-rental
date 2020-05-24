from flask_restful import Resource
from flask import request

from rentalapi.dao.models import Rentals
from rentalapi.schema import RentalSchema

rental_schema = RentalSchema()
rentals_schema = RentalSchema(many=True)


class RentalsAPI(Resource):
    def get(self):
        rentals = Rentals.query.all()

        return rentals_schema.dump(rentals)


class RentalAPI(Resource):
    def get(self, rental_id):
        rental = Rentals.query.filter_by(id=rental_id).first()

        if not rental:
            abort(
                404,
                message="rental id {} doesn't exist".format(rental_id))

        return rental_schema.dump(rental)

    def post(self):
        data = request.get_json()

        rental, errors = rental_schema.load(data)

        if errors:
            abort(422, message=errors)

        try:
            db.session.add(rental)
            db.session.commit()
        except:
            db.sessoion.rollback()

        return rental_schema.dump(rental)

    def put(self, rental_id):
        rental = Rentals.query.get(rental_id)

        if not rental:
            abort(
                404,
                message="rental id {} doesn't exist".format(rental_id))

        data = request.json()
        put_rental, errors = rental_schema.load(data)

        if errors:
            abort(422, message=errors)

        rental.name = put_rental.name

        try:
            db.session.commit()
        except:
            db.session.rollback()

        return rental_schema.dump(rental)

    def delete(self, rental_ud):
        rental = Rentals.query.get(rental_id)

        if not rental:
            abort(
                404,
                message="rental id {} doesn't exist".format(rental_ud)
                )

        try:
            db.session.delete(rental)
            db.session.commit()
        except:
            db.session.rollback()

        return rental_schema.dump(rental)
