from . import celery
import time

@celery.task()
def add(a, b):
  time.sleep(30)
  return a + b