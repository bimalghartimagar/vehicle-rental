from flask_restful import Resource, abort
from flask import current_app, request
from marshmallow import ValidationError

from rentalapi.dao.models import Vendors
from rentalapi.schema import VendorSchema
from rentalapi.dao.models import db

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)


class VendorsAPI(Resource):
    def get(self):
        vendors = Vendors.query.all()

        return vendors_schema.dump(vendors)

    def post(self):
        data = request.get_json()

        try:
            vendor = vendor_schema.load(data)
            current_app.logger.debug(vendor)
        except ValidationError as err:
            current_app.logger.debug(err.messages)
            current_app.logger.debug(err.valid_data)
            abort(422, message=err.messages)

        try:
            db.session.add(vendor)
            db.session.commit()
        except Exception as err:
            current_app.logger.debug(err)
            db.session.rollback()

        return vendor_schema.dump(vendor)

class VendorAPI(Resource):
    def get(self, vendor_id):
        vendor = Vendors.query.filter_by(id=vendor_id).first()

        if not vendor:
            abort(
                404,
                message="Vendor id {} doesn't exist".format(vendor_id))

        return vendor_schema.dump(vendor)

    def put(self, vendor_id):
        vendor = Vendors.query.get(vendor_id)

        if not vendor:
            abort(
                404,
                message="Vendor id {} doesn't exist".format(vendor_id))

        data = request.get_json()

        try:
            put_vendor = vendor_schema.load(data)
        except ValidationError as err:
            current_app.logger.debug(err.messages)
            current_app.logger.debug(err.valid_data)
            abort(422, message=err.messages)

        vendor.name = put_vendor.name

        try:
            db.session.commit()
        except Exception as err:
            current_app.logger.debug(err)
            db.session.rollback()

        return vendor_schema.dump(vendor)

    def delete(self, vendor_id):
        vendor = Vendors.query.get(vendor_id)

        if not vendor:
            abort(
                404,
                message="Vendor id {} doesn't exist".format(vendor_ud)
                )

        try:
            db.session.delete(vendor)
            db.session.commit()
        except:
            db.session.rollback()

        return vendor_schema.dump(vendor)
