from flask import Flask
app = Flask(__name__)

from ppserver.pixel.controllers import pixel
app.register_blueprint(pixel)


import views
