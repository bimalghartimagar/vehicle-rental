from flask import jsonify, request

from rentalapi.schema import SearchSchema
from rentalapi.dao.models import Vehicles, Rentals

vehicles_schema = SearchSchema(many=True)

api = None

def init_search(api_bp):
  api = api_bp
  
  @api.route('/search/vehicles')
  def search():
    pickup = request.args.get('pickup')
    dropoff = request.args.get('dropoff')
    pickup_date = request.args.get('pickupDate')
    dropoff_date = request.args.get('dropoffDate')
    age = request.args.get('age')
    
    query = Vehicles.query.join(Rentals, Vehicles.id==Rentals.vehicle_id, isouter=True)
    query = query.filter(
      (Rentals.pickup_date == None) | 
      (~Rentals.pickup_date.between(pickup_date, dropoff_date)) &
      (~Rentals.dropoff_date.between(pickup_date, dropoff_date))
    )
    vehicles = query.all()
    return jsonify(vehicles_schema.dump(vehicles))
