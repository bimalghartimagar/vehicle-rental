from flask_restful import Resource, abort
from flask import current_app, request
from marshmallow import ValidationError
from flask_jwt_extended import (jwt_required)

from rentalapi.dao.models import Vehicles, Vendors
from rentalapi.schema import VehicleSchema
from rentalapi.dao.models import db

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)


class VehiclesAPI(Resource):
    @jwt_required()
    def get(self):
        vehicles = Vehicles.query.all()

        return vehicles_schema.dump(vehicles)
    
    def post(self):
        data = request.get_json()
        current_app.logger.debug('data')
        current_app.logger.debug(data)

        try:
            # vendor = Vendors.query.get(data['vendor'])
            # current_app.logger.debug('vendor fetched')
            # current_app.logger.debug(vendor)
            # data['vendor'] = vendor
            vehicle = vehicle_schema.load(data)
        except ValidationError as err:
            current_app.logger.debug(err.messages)
            current_app.logger.debug(err.valid_data)
            abort(422, message=err.messages)

        try:
            db.session.add(vehicle)
            db.session.commit()
        except Exception as err:
            current_app.logger.debug(err)
            db.session.rollback()

        return vehicle_schema.dump(vehicle)


class VehicleAPI(Resource):
    def get(self, vehicle_id):
        vehicle = Vehicles.query.filter_by(id=vehicle_id).first()

        if not vehicle:
            abort(
                404,
                message="vehicle id {} doesn't exist".format(vehicle_id))

        return vehicle_schema.dump(vehicle)

    def put(self, vehicle_id):
        vehicle = Vehicles.query.get(vehicle_id)

        if not vehicle:
            abort(
                404,
                message="vehicle id {} doesn't exist".format(vehicle_id))
        
        data = request.get_json()

        try:
            put_vehicle = vehicle_schema.load(data)
        except ValidationError as err:
            current_app.logger.debug(err.messages)
            current_app.logger.debug(err.valid_data)
            abort(422, message=err.messages)

        vehicle.name = put_vehicle.name
        vehicle.seats = put_vehicle.seats
        vehicle.color = put_vehicle.color
        vehicle.make_year = put_vehicle.make_year
        vehicle.rate = put_vehicle.rate
        vehicle.type = put_vehicle.type
        vehicle.vendor_id = put_vehicle.vendor_id

        try:
            db.session.commit()
        except Exception as err:
            current_app.logger.debug(err)
            db.session.rollback()

        return vehicle_schema.dump(vehicle)

    def delete(self, vehicle_id):
        vehicle = Vehicles.query.get(vehicle_id)

        if not vehicle:
            abort(
                404,
                message="vehicle id {} doesn't exist".format(vehicle_id)
                )

        try:
            db.session.delete(vehicle)
            db.session.commit()
        except:
            db.session.rollback()

        return vehicle_schema.dump(vehicle)
