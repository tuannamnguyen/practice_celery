from celery import shared_task, chain


@shared_task()
def test1():
    return "abcdef"

@shared_task()
def test2(a: str):
    return f"{a} deeznuts on the ballots"


@shared_task()
def test3():
    chain(test1.s(), test2.s()).apply_async()