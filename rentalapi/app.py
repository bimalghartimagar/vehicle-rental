import os
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from celery import Celery

from .dao.models import db, migrate, Vendors, Vehicles, Users, UserTypes
from . import config

from rentalapi.utils.jwtauth import jwt
from rentalapi.schema import ma
from rentalapi.api import api_bp
from rentalapi.celery_util import init_celery
from rentalapi.auth import auth_bp

from . import celery

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
    
    app.app_context().push()

    init_celery(celery, app)

    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()

    ma.init_app(app)

    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    
    cors = CORS(app)

    @app.after_request
    def after_request(response):
        if request.method == "OPTIONS":
            return app.response_class(response=response.data, status=200)
        else:
            return response

    if app.config['ENV'] == 'development':
        from .dummy_data import insert_dummy_data
        app.cli.add_command(insert_dummy_data)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        app.logger.error('Error while creating instance path directory')
        import traceback
        traceback.print_exc(file='error.log')

    @app.route('/')
    def home():
        return json.dumps(
                    {
                        "message": "Welcome to Vehicle Rental API.",
                        "url": "{}api/".format(request.base_url)
                    }
                )

    return app


if __name__ == '__main__':
    create_app().run()
