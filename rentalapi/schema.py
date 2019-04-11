from flask_marshmallow import Marshmallow

from rentalapi.dao.models import Vendors
from rentalapi.dao.models import UserTypes

ma = Marshmallow()


class VendorSchema(ma.ModelSchema):
    class Meta:
        model = Vendors


class UserTypeSchema(ma.ModelSchema):
    class Meta:
        model = UserTypes
