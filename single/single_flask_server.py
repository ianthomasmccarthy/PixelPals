from flask import Flask
from pixelpal import PixelPal

app = Flask(__name__)
pp = PixelPal()


@app.route("/")
def hello(self):
    return "Hello World!"


@app.route("/toggle")
def toggle(self):
    app.toggle()
    return 'Toggle'


@app.route('/on')
def on(self):
    if not pp.state:
        pp.toggle()
    return 'on'


@app.route('/off')
def off():
    if pp.state:
        pp.toggle()
    return 'off'


@app.route('/status')
def status(self):
    return str(pp.status)


if __name__ == '__main__':
    app.run()
