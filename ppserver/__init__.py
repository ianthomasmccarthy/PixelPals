from flask import Flask
from celery import Celery
app = Flask(__name__)
app.config.from_object('config.Config')
from ppserver.pixel.models import PPFeedback
pp = PPFeedback()
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from ppserver.pixel.controllers import pixel
app.register_blueprint(pixel)




import views
