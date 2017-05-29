from flask import Flask
from celery import Celery

app = Flask(__name__)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from ppserver.pixel.controllers import pixel
app.register_blueprint(pixel)


import views
