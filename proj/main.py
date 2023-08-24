from celery import Celery

app = Celery(
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['proj.tasks']
)

app.conf.beat_schedule = {
    'test_beat': {
        'task': 'add',
        'schedule': 10.0,
    },
}


