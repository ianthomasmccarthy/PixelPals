from flask import Flask
from pixelpal import PixelPal



class test(object):

    def init(self):
        self.app = Flask(__name__)
        self.pp = PixelPal()

    @self.app.route("/")
    def hello(self):
        return "Hello World!"


    @self.app.route("/toggle")
    def toggle(self):
        self.pp.toggle()
        return 'Toggle'


    @self.app.route('/on')
    def on(self):
        if not self.pp.status:
            self.pp.toggle()
        return 'on'


    @self.app.route('/off')
    def off(self):
        if self.pp.status:
            self.pp.toggle()
        return 'off'


    @self.app.route('/status')
    def status(self):
        return str(self.pp.status)

if __name__ == "__main__":
    t = test()

    test.app.run()
