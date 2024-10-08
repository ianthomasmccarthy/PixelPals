#!/opt/pixelpals/venv/bin/python

import requests
from time import sleep
import optparse
import logging
from logging.handlers import TimedRotatingFileHandler
import sys
sys.path.append('/opt/pixelpals')
from pixelpal import PixelPal
from config import Config


class PixelPalRunner(object):

    def __init__(self):
        # Default Values
        self.delay    = 20
        self.url      = 'http://192.168.1.11/pixel/checkin'
        self.log_file = '/opt/pixelpals/logs/PixelPalRunner.log'
        self.pp       = PixelPal()

    def logging_setup(self, log_file):
        self.logger = logging.getLogger()
        handler = TimedRotatingFileHandler(log_file, when="D",
                                           interval=1, backupCount=2)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def get_parser(self):
        return optparse.OptionParser()

    def options(self):
        parser = self.get_parser()
        parser.add_option('-H', '--host-name',   action='store', dest='hostname', help='Systems Hostname')
        parser.add_option('-U', '--url-checkin', action='store', dest='url',      help='Url Checkin')
        parser.add_option('-D', '--delay',       action='store', dest='delay',    help='delay between url checks' ),
        parser.add_option('-L', '--log-file',    action='store', dest='log',      help='log location' ),
        # retrive options
        (options, args) = parser.parse_args()
        # If we have command line options use instead of default value.
        self.hostname = options.hostname
        self.url      = options.url if options.url else self.url
        self.delay    = options.delay if options.delay else 20
        self.log_file = options.log if options.log else self.log_file

    def check_url(self, url, hostname):
        try:
            self.logger.info('checking this url: {url}'.format(url=url))
            udata = requests.get(url)
        except Exception as e:
            self.logger.error(e)
            if self.pp.state:
                return True
            else:
                return False
        udata = str(udata.text).lower()
        self.logger.info('Webdata is: {d}'.format(d=udata))
        if hostname.lower() in udata:
            self.logger.info('check_url is true')
            return True
        else:
            self.logger.info('check_url is false')
            return False

    def main(self):
        self.options()
        self.logging_setup(log_file=self.log_file)
        self.logger.info('Startup PixelPalRunner')
        while True:
            sleep(self.delay)
            if Config.JUST_ON:
                if not self.pp.state: self.pp.toggle()
            if self.check_url(url=self.url, hostname=self.hostname):
                if not self.pp.state:
                    self.pp.toggle()
            else:
                if self.pp.state:
                    self.pp.toggle()

if __name__ == '__main__':
    ppr = PixelPalRunner()
    ppr.main()
