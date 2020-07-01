from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required, 
    jwt_refresh_token_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_raw_jwt
)

import datetime
from rentalapi.utils.jwtauth import jwt
from rentalapi.dao.models import Users, db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

blacklist = set()

token_expiry_minutes = 1

@jwt.token_in_blacklist_loader
def is_token_blacklist(decrypted_token):
  jti = decrypted_token['jti']
  return jti in blacklist

@auth_bp.route('/login/', methods=['POST'])
def login():
  if not request.is_json:
    return jsonify({'msg': 'Missing JSON in request'}), 400

  username = request.json.get('username', None)
  password = request.json.get('password', None)
  if not username or not password:
    return jsonify({'msg': 'Invalid credentials.'}), 401

  user = Users.query.filter_by(username=username).first()
  if not user:
    return jsonify({'msg': 'Invalid credentials.'}), 401

  authorized = user.check_password(password)
  if not authorized:
    return jsonify({'msg': 'Invalid credentials.'}), 401

  expires = datetime.timedelta(minutes=token_expiry_minutes)

  access_token = create_access_token(identity=username, expires_delta=expires, fresh=True)
  refresh_token = create_refresh_token(identity=username)
  return jsonify(access_token=access_token, refresh_token=refresh_token), 200

@auth_bp.route('/signup/', methods=['POST'])
def signup():
  if not request.is_json:
    return jsonify({'msg': 'Missing JSON in request'}), 400
  
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

@auth_bp.route('/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh():
  current_user = get_jwt_identity()
  expires = datetime.timedelta(minutes=token_expiry_minutes)
  return jsonify({
    'access_token': create_access_token(identity=current_user, expires_delta=expires, fresh=False)
  })
  pass

@auth_bp.route('/logout/', methods=['DELETE'])
@jwt_required
def logout():
  jti = get_raw_jwt()['jti']
  blacklist.add(jti)
  return jsonify({
    'msg': 'Logged out successfully.'
  }), 200

@auth_bp.route('/logout2/', methods=['DELETE'])
@jwt_refresh_token_required
def logout2():
  jti = get_raw_jwt()['jti']
  blacklist.add(jti)
  return jsonify({
    'msg': 'Logged out successfully.'
  }), 200