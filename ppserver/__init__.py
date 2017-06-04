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


import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler(app.config.get('LOG_PATH'), 'a',
                                   1 * 1024 * 1024, 10)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('PixelServer startup')

import views
