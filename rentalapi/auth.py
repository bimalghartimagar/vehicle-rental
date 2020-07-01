from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required, 
    create_access_token,
    get_jwt_identity
)
import datetime

from rentalapi.dao.models import Users, db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login/', methods=["POST"])
def login():
  if not request.is_json:
    return jsonify({"msg": "Missing JSON in request"}), 400

  username = request.json.get('username', None)
  password = request.json.get('password', None)
  if not username or not password:
    return jsonify({"msg": "Bad credentials"}), 400

  user = Users.query.filter_by(username=username).first()
  if not user:
    return jsonify({"msg": "Bad credentials"}), 400

  authorized = user.check_password(password)
  if not authorized:
    return jsonify({'msg': 'Email or password invalid'}), 400

  expires = datetime.timedelta(minutes=15)

  access_token = create_access_token(identity=username, expires_delta=expires)
  return jsonify(access_token=access_token), 200

@auth_bp.route("/signup/", methods=["POST"])
def signup():
  if not request.is_json:
    return jsonify({"msg": "Missing JSON in request"}), 400
  
  username = request.json.get('username', None)
  password = request.json.get('password', None)

  user = Users(**request.get_json())
  user.hash_password()

  try:
    db.session.add(user)
    db.session.commit()
  except:
    db.session.rollback()

  return jsonify({'msg': 'Successfully registered. Login to use the application.'}), 200

@auth_bp.route("/refresh/")
def refresh():
  pass