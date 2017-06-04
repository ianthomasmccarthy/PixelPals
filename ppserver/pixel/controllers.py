from flask import Blueprint
from ppserver.pixel.tasks import pixel_time
from ppserver import app, pp

pixel = Blueprint('pixel',
                  __name__,
                  url_prefix='/pixel',
                  template_folder='templates/pixel')


@pixel.route('/')
def index():
    return 'Hello'


@pixel.route('/on')
def on():
    app.logger.info('Running on endpoint')
    pp.on()
    return "good"


@pixel.route('/off')
def off():
    app.logger.info('Running off endpoint')
    pp.off()
    return 'good'


@pixel.route('/checkin')
def checkin():
    app.logger.info('Running on endpoint with: {p}'.format(p=str(pp)))
    return str(pp)


@pixel.route('/pixel/time/<int:mins>')
def pixtime(mins):
    pixel_time.apply_async(args=[mins])
    return 'good'
