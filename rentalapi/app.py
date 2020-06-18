import os
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .dao.models import db, migrate, Vendors, Vehicles, Users, UserTypes
from . import config

from rentalapi.schema import ma
from rentalapi.api import api_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.app_context().push()

    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()

    ma.init_app(app)

    app.register_blueprint(api_bp)
    
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        # response.headers.add('Access-Control-Allow-Origin', '*')
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        # response.headers.add('Access-Control-Allow-Credentials', 'true')
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
