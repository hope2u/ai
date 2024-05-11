import os
from flask import flask

app = flask(__name__)

app.config['SECRET_KEY'] = 'any string works here'

from app import views.auto.py