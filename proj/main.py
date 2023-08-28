from celery import Celery, signature


app = Celery(
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['proj.tasks']
)

app.conf.beat_schedule = {
    'test_beat': {
        'task': 'proj.tasks.test1',
        'schedule': 3.0,
        'options': {
            'link': signature('proj.tasks.test2', immutable=True)
        }
    },
}
