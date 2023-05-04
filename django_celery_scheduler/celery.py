from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_scheduler.settings')
app = Celery('django_celery_scheduler')
app.conf.enable_utc = False
app.conf.update(timezone='Africa/Dar_es_Salaam')
app.config_from_object(settings, namespace='CELERY')

##selecry beat settings

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')