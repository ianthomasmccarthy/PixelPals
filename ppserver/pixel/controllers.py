from flask import Blueprint

pixel = Blueprint('pixel',
                  __name__,
                  template_folder='templates/pixel')

@pixel.route('/')
def index():
    return 'Hello'