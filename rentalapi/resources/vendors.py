from flask_restful import Resource

from rentalapi.dao.models import Vendors
from rentalapi.schema import VendorSchema

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)


class Vendor(Resource):
    def get(self):
        vendors = Vendors.query.all()

        return vendors_schema.dump(vendors).data

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
