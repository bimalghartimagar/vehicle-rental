from celery import Celery

from flask import current_app


def init_celery(app):
    celery = Celery(
        __name__,
        backend=current_app.config['CELERY_RESULT_BACKEND'],
        broker=current_app.config['CELERY_BROKER_URL'],
        include=['rentalapi.celery_tasks']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
