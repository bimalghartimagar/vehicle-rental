from flask_marshmallow import Marshmallow
from marshmallow import post_load

from rentalapi.dao.models import Vendors, UserTypes, Vehicles, Users, Rentals

ma = Marshmallow()


class IndexSchema(ma.SQLAlchemyAutoSchema):
    vendors = ma.URLFor('api.vendorsapi', _external=True)
    vehicles = ma.URLFor('api.vehiclesapi', _external=True)
    users = ma.URLFor('api.usersapi', _external=True)
    usertypes = ma.URLFor('api.usertypesapi', _external=True)
    rentals = ma.URLFor('api.rentalsapi', _external=True)


class VendorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vendors

    vehicles = ma.List(
                        ma.HyperlinkRelated(
                            'api.vehicleapi',
                            'vehicle_id',
                            True)
                        )
    @post_load
    def make_object(self, data, **kwargs):
        return Vendors(**data)


class UserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserTypes

    users = ma.List(
                    ma.HyperlinkRelated(
                        'api.userapi',
                        'user_id',
                        external=True)
                    )
    @post_load
    def make_object(self, data, **kwargs):
        return UserTypes(**data)


class VehicleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehicles
        include_fk = True

    vendor = ma.Nested(VendorSchema, exclude = ('vehicles',))

    @post_load
    def make_object(self, data, **kwargs):
        return Vehicles(**data)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

    usertype = ma.HyperlinkRelated(
                'api.usertypeapi',
                'user_type_id',
                external=True
                )


class RentalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rentals
