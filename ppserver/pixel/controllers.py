from flask import Blueprint
from ppserver.pixel.tasks import long_task

pixel = Blueprint('pixel',
                  __name__,
                  url_prefix='/pixel',
                  template_folder='templates/pixel')


@pixel.route('/')
def index():
    return 'Hello'


@pixel.route('/long')
def long():
    long_task.apply_async()
    return 'Started Long task, check log.'


@pixel.route('/check')
def check():
    raise Exception('REally WiErd Fucking error.')
    return 'blah'
