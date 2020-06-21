#!/usr/bin/env python

from ..rentalapi import celery
from .app import create_app

app = create_app()
app.app_context().push()
