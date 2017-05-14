import RPi.GPIO as GPIO
import time
import os

class PixelPal(object):
    def __init__(self):
	self.pixel_pal_pin = 24
        self.state = False
        self.setup_gpio()
        self.toggle()


    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pixel_pal_pin, GPIO.OUT, initial=0)
        self.state = False

    def _off(self):
        GPIO.output(self.pixel_pal_pin, 0)
        self.state = False

    def _on(self):
        GPIO.output(self.pixel_pal_pin, 1)
        self.state = True

    def toggle(self):
        if self.state:
            self._off()
        else:
            self._on()
    def error(self):
        if self.state:
            self._off()
        GPIO.cleanup()

    @property
    def status(self):
        if self.state:
            return 'On'
        else:
            return 'Off'

    @property
    def pin(self):
        return self.pixel_pal_pin

    def __str__(self):
        return 'Pixel Pal, Pin: {p} Status: {s}'.format(p=self.pin, s=self.state)

    def __repr__(self):
        return 'Pixel Pal, Pin: {p} Status: {s}'.format(p=self.pin, s=self.state)

if __name__ == '__main__':
    bit = PixelPal()
    while True:
        try:
            bit.toggle()
        except KeyboardInterrupt:
            bit.error()
