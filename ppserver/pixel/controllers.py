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
    pp.on()
    return "good"


@pixel.route('/off')
def off():
    pp.off()
    return 'good'


@pixel.route('/checkin')
def checkin():
    return str(pp)


@pixel.route('/pixeltime/<int:mins>')
def pixtime(mins):
    pixel_time.apply_async(args=[mins])
    return 'good'
