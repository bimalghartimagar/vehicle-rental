from celery import Celery

from . import config

celery = Celery(
  __name__,
  backend=config.CELERY_RESULT_BACKEND,
  broker=config.CELERY_BROKER_URL,
  include=['rentalapi.celery_tasks']
)