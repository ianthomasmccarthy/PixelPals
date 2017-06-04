from flask import Flask
from celery import Celery

#  Create App
app = Flask(__name__)
app.config.from_object('config.Config')

# Create pp return
from ppserver.pixel.models import PPFeedback
pp = PPFeedback()

# Create Celery object
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Create Blueprints
from ppserver.pixel.controllers import pixel
app.register_blueprint(pixel)

import views
