from flask_restful import Resource
from flask import request

from rentalapi.dao.models import Vendors
from rentalapi.schema import VendorSchema

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)


class VendorsAPI(Resource):
    def get(self):
        vendors = Vendors.query.all()

        return vendors_schema.dump(vendors).data


class VendorAPI(Resource):
    def get(self, vendor_id):
        vendor = Vendors.query.filter_by(id=vendor_id).first()

        if not vendor:
            abort(
                404,
                message="Vendor id {} doesn't exist".format(vendor_id))

        return vendor_schema.dump(vendor).data

    def post(self):
        data = request.get_json()

        vendor, errors = vendor_schema.load(data)

        if errors:
            abort(422, message=errors)

        try:
            db.session.add(vendor)
            db.session.commit()
        except:
            db.sessoion.rollback()

        return vendor_schema.dump(vendor).data

    def put(self, vendor_id):
        vendor = Vendors.query.get(vendor_id)

        if not vendor:
            abort(
                404,
                message="Vendor id {} doesn't exist".format(vendor_id))

        data = request.json()
        put_vendor, errors = vendor_schema.load(data)

        if errors:
            abort(422, message=errors)

        vendor.name = put_vendor.name

        try:
            db.session.commit()
        except:
            db.session.rollback()

        return vendor_schema.dump(vendor).data

    def delete(self, vendor_ud):
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

        return vendor_schema.dump(vendor).data
