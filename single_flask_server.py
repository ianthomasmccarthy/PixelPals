from flask import Flask
from pixelpal import PixelPal



class test(object):

    app = Flask(__name__)

    def __init__(self):
        self.pp = PixelPal()

    @app.route("/")
    def hello(self):
        return "Hello World!"


    @app.route("/toggle")
    def toggle(self):
        self.pp.toggle()
        return 'Toggle'


    @app.route('/on')
    def on(self):
        if not self.pp.status:
            self.pp.toggle()
        return 'on'


    @app.route('/off')
    def off(self):
        if self.pp.status:
            self.pp.toggle()
        return 'off'


    @app.route('/status')
    def status(self):
        return str(self.pp.status)

if __name__ == "__main__":
    t = test()
    test.app.run()
