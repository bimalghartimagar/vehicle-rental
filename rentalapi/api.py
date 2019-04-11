from flask import Blueprint
from flask_restful import Api, url_for

from rentalapi.resources.vendors import Vendor

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp)

api.add_resource(Vendor, '/vendors/')
