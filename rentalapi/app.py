import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        app.logger.error('Error while creating instance path directory')
        import traceback
        traceback.print_exc(file='error.log')

    @app.route('/')
    def home():
        return 'Welcome to Vehicle Rental API.'

    return app

if __name__ == '__main__':
    create_app.run()
