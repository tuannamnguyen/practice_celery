from celery import shared_task, chain
from proj.main import app


@shared_task()
def add(x, y):
    return x + y


@shared_task()
def test():
    return "deez nuts on the ballots"


# add.signature((5, 3)).apply_async(link=test.signature(immutable=True))
# test.si().delay()
# add.s(5, 3).delay()
chained_task = chain(add.s(5, 3), test.si())

print(add.apply_async(args=[5, 3]))
print(test.apply_async())
print(chained_task)
