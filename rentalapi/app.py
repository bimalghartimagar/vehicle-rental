import os
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from .dao.models import db, Vendors, Vehicles, Users, UserTypes
from . import config

from rentalapi.schema import ma
from rentalapi.api import api_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.app_context().push()

    db.init_app(app)
    db.create_all()

    ma.init_app(app)

    app.register_blueprint(api_bp)

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
