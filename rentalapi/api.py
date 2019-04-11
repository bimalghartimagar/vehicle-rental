from flask import Blueprint
from flask_restful import Api, url_for

from rentalapi.resources.vendors import VendorAPI
from rentalapi.resources.usertypes import UserTypesAPI
api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp)

api.add_resource(VendorAPI, '/vendors/')
api.add_resource(UserTypesAPI, '/usertype/', '/usertype/<int:user_type_id>/')
