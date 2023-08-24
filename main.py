from celery import Celery, shared_task, chain
from celery.schedules import crontab

app = Celery(
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


# @shared_task()
@app.task
def add(x, y):
    return x + y

# @shared_task()
@app.task
def test():
    return "deez nuts on the ballots"


# add.signature((5, 3)).apply_async(link=test.signature(immutable=True))
# test.si().delay()
# add.s(5, 3).delay()
chained_task = chain(add.s(5, 3), test.si())



app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'main.add',
        'schedule': 10.0,
        'args': (1, 2)
    },
}

print(chained_task)
print(add.s(5, 3))
print(test.si())

