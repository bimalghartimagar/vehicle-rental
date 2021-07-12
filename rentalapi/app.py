import os
import json

from flask import Flask, request
from flask_cors import CORS

from rentalapi.dao.models import db, migrate

from rentalapi.utils.jwtauth import jwt
from rentalapi.schema import ma
from rentalapi.api import api_bp
from rentalapi.celery_util import init_celery
from rentalapi.auth import auth_bp

def create_app(config_filename=None):
    app = Flask(__name__, instance_path=f'{os.getcwd()}{os.sep}instance', instance_relative_config=True)

    app.config.from_pyfile(config_filename)

    app.app_context().push()

    init_extensions(app)

    register_blueprints(app)

    cors = CORS(app)

    @app.after_request
    def after_request(response):
        if request.method == "OPTIONS":
            return app.response_class(response=response.data, status=200)
        else:
            return response

    if app.config['ENV'] == 'development':
        from .seed_data import insert_dummy_data, seed_data
        app.cli.add_command(insert_dummy_data)
        app.cli.add_command(seed_data)
    elif app.config['ENV'] == 'production':
        from .seed_data import seed_prod_data
        seed_prod_data()

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


def init_extensions(app) -> None:
    init_celery(app)

    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()

    ma.init_app(app)

    jwt.init_app(app)


def register_blueprints(app) -> None:
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)


if __name__ == '__main__':
    create_app('dev.cfg').run()
