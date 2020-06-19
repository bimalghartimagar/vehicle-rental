from flask_restful import Resource
from flask import request

from rentalapi.dao.models import Vehicles
from rentalapi.schema import VehicleSchema

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)


class VehiclesAPI(Resource):
    def get(self):
        vehicles = Vehicles.query.all()

        return vehicles_schema.dump(vehicles)


class VehicleAPI(Resource):
    def get(self, vehicle_id):
        vehicle = Vehicles.query.filter_by(id=vehicle_id).first()

        if not vehicle:
            abort(
                404,
                message="vehicle id {} doesn't exist".format(vehicle_id))

        return vehicle_schema.dump(vehicle)

    def post(self):
        data = request.get_json()

        vehicle, errors = vehicle_schema.load(data)

        if errors:
            abort(422, message=errors)

        try:
            db.session.add(vehicle)
            db.session.commit()
        except:
            db.session.rollback()

        return vehicle_schema.dump(vehicle)

    def put(self, vehicle_id):
        vehicle = Vehicles.query.get(vehicle_id)

        if not vehicle:
            abort(
                404,
                message="vehicle id {} doesn't exist".format(vehicle_id))
        
        data = request.json()
        put_vehicle, errors = vehicle_schema.load(data)

        if errors:
            abort(422, message=errors)

        vehicle.name = put_vehicle.name

        try:
            db.session.commit()
        except:
            db.session.rollback()

        return vehicle_schema.dump(vehicle)

    def delete(self, vehicle_ud):
        vehicle = Vehicles.query.get(vehicle_id)

        if not vehicle:
            abort(
                404,
                message="vehicle id {} doesn't exist".format(vehicle_ud)
                )

        try:
            db.session.delete(vehicle)
            db.session.commit()
        except:
            db.session.rollback()

        return vehicle_schema.dump(vehicle)
