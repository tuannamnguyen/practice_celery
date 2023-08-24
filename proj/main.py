from celery import Celery, signature


app = Celery(
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['proj.tasks']
)

app.conf.beat_schedule = {
    'test_beat': {
        'task': 'proj.tasks.add',
        'schedule': 5.0,
        'args': (1, 2),

        'options': {
            'link': signature('proj.tasks.test', immutable=True)
        }
    },
}
