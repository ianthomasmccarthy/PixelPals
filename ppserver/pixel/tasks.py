
from celery import Celery
import requests


@celery.task(bind=True)
def long_task(self):
    c = 0
    while c != 100:
        c += 1
        time.sleep(1)
        self.update_state(state='PROGRESS',
                          meta={'current': i,
                                'total': 10,
                                'status': 'working...'}
                        )
    request.get('127.0.0.1/pixel/check')
    return {'current': i,
            'total': i,
            'status': 'Task Complete',
            'result': 'Go Away!'
            }
