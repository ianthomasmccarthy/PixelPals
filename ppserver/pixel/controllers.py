from flask import Blueprint

pixel = Blueprint('pixel',
                  __name__,
                  url_prefix='/pixel',
                  template_folder='templates/pixel')

@pixel.route('/')
def index():
    return 'Hello'
