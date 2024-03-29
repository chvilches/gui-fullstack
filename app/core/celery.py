
from datetime import timedelta
import os

from celery import Celery
from celery.signals import setup_logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')  

app.conf.broker_url = 'redis://redis:6379/0'
app.conf.broker_connection_retry_on_startup = True


app.config_from_object('django.conf:settings', namespace='CELERY')



app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-hour': {
        'task': 'welcome.tasks.add',
        'schedule': timedelta(minutes=60),
        'args': (16, 1)
    },

}

@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig  # noqa
    from django.conf import settings  # noqa

    dictConfig(settings.LOGGING)

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    print(f'Request: *************************************************')