from celery import shared_task


@shared_task()
def test1():
    return "abcdef"

@shared_task()
def test2():
    return "ghijkl"
