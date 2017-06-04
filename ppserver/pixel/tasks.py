import time
from ppserver import celery, app
import requests
from random import randint
# from celery import Celery


@celery.task(bind=True)
def long_task(self):
    """My long task."""
    c = 0
    while c != 100:
        c += 1
        i = randint(0, 10)
        time.sleep(1)
        self.update_state(state='PROGRESS',
                          meta={'current': i,
                                'total': 10,
                                'status': 'working...'}
                          )
    requests.get('127.0.0.1/pixel/check')
    return {'current': i,
            'total': i,
            'status': 'Task Complete',
            'result': 'Go Away!'
            }


@celery.task(bind=True)
def pixel_time(self, mins):
    app.logger.info('Running get request to turn on')
    try:
        requests.get('http://192.168.1.11/pixel/on')
    except Exception as e:
        app.logger.error(e)
    c = 0
    app.logger.info( 'Delay time is: {t}'.format( t=mins*60 ) )
    while c != (mins * 60):
        c += 1
        i = randint(0, 10)
        time.sleep(1)
        self.update_state(state='PROGRESS',
                          meta={'current': i,
                                'total': 10,
                                'status': 'working...'}
                          )
    requests.get('http://192.168.1.11/pixel/off')
