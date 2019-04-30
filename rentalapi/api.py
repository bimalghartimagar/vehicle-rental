from flask import Blueprint
from flask_restful import Api, url_for

from rentalapi.resources.vendors import VendorsAPI, VendorAPI
from rentalapi.resources.rentals import RentalsAPI, RentalAPI
from rentalapi.resources.users import UsersAPI, UserAPI
from rentalapi.resources.vehicles import VehiclesAPI, VehicleAPI
from rentalapi.resources.usertypes import UserTypesAPI, UserTypeAPI
from rentalapi.resources.index import IndexAPI

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp)

api.add_resource(IndexAPI, '/')

api.add_resource(VendorsAPI, '/vendors/')
api.add_resource(VendorAPI, '/vendor/<int:vendor_id>/')

api.add_resource(UsersAPI, '/users/')
api.add_resource(UserAPI, '/user/<int:user_id>/')

api.add_resource(VehiclesAPI, '/vehicles/')
api.add_resource(VehicleAPI, '/vehicle/<int:vehicle_id>/')

api.add_resource(RentalsAPI, '/rentals/')
api.add_resource(RentalAPI, '/rental/<int:rental_id>/')

api.add_resource(UserTypesAPI, '/usertypes/')
api.add_resource(UserTypeAPI, '/usertype/<int:user_type_id>/')
