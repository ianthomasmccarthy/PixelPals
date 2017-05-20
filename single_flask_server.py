from flask import Flask
from pixelpal import PixelPal

app = Flask(__name__)
pp = PixelPal()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/toggle")
def toggle():
    pp.toggle()
    return 'Toggle'

@app.route('/on')
def on():
    if not pp.status:
        pp.toggle()
    return 'on'

@app.route('/off')
def off():
    if pp.status:
        pp.toggle()
    return 'off'

@app.route('/status')
def status():
    return str(pp.status)

if __name__ == "__main__":
    app.run()
