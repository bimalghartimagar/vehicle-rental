from flask_marshmallow import Marshmallow

from rentalapi.dao.models import Vendors

ma = Marshmallow()


class VendorSchema(ma.ModelSchema):
    class Meta:
        model = Vendors
