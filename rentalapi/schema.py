from flask_marshmallow import Marshmallow

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


class UserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserTypes

    users = ma.List(
                    ma.HyperlinkRelated(
                        'api.userapi',
                        'user_id',
                        external=True)
                    )


class VehicleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehicles

    vendor = ma.HyperlinkRelated(
                'api.vendorapi',
                'vendor_id',
                external=True
                )


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
