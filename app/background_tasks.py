'''
from celery import Celery
from datetime import timedelta

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def clear_data():
    # Очистка данных
    pass

app.conf.beat_schedule = {
    'clear-data-every-week': {
        'task': 'tasks.clear_data',
        'schedule': timedelta(weeks=1),
    },
}
'''