from flask import jsonify, current_app
from rentalapi.schema import SearchSchema
from rentalapi.dao.models import Vehicles

vehicles_schema = SearchSchema(many=True)

api = None

def init_search(api_bp):
  api = api_bp
  
  @api.route('/search/vehicles')
  def search():
    current_app.logger.debug('Searching')
    vehicles = Vehicles.query.all()
    current_app.logger.debug('Fetched')
    results = jsonify(vehicles_schema.dump(vehicles))
    # return vehicles_schema.dump(vehicles)
    return results
