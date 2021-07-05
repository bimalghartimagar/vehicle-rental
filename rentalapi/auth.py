from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required, 
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt
)

import datetime
from rentalapi.utils.jwtauth import jwt
from rentalapi.dao.models import Users, db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

blocklist = set()

token_expiry_minutes = 120

@jwt.user_identity_loader
def user_identity_lookup(user):
  return user.username+':'+str(user.id)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
  identity = jwt_data['sub']
  user = identity.split(':')
  return Users.query.filter_by(username=user[0], id=user[1]).one_or_none()

@jwt.user_lookup_error_loader
def custom_user_lookup_error_loader(_jwt_header, jwt_data):
    return jsonify({"msg": "User not authorized"}), 401

@jwt.token_in_blocklist_loader
def is_token_blocklist(jwt_header, jwt_data):
  jti = jwt_data['jti']
  return jti in blocklist

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

  access_token = create_access_token(identity=user, expires_delta=expires, fresh=True)
  refresh_token = create_refresh_token(identity=user)
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
    return jsonify({'msg': 'Successfully registered. Login to use the application.'}), 200
  except Exception as e:
    db.session.rollback()
    return jsonify({'error': str(e)}), 400

@auth_bp.route('/refresh/', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
  current_user = get_jwt_identity()
  expires = datetime.timedelta(minutes=token_expiry_minutes)
  return jsonify({
    'access_token': create_access_token(identity=current_user, expires_delta=expires, fresh=False)
  })
  pass

@auth_bp.route('/logout/', methods=['DELETE'])
@jwt_required()
def logout():
  jti = get_jwt()['jti']
  blocklist.add(jti)
  return jsonify({
    'msg': 'Logged out successfully.'
  }), 200

@auth_bp.route('/logout2/', methods=['DELETE'])
@jwt_required(refresh=True)
def logout2():
  jti = get_jwt()['jti']
  blocklist.add(jti)
  return jsonify({
    'msg': 'Logged out successfully.'
  }), 200