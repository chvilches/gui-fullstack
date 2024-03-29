from celery import Celery

app = Celery()


@app.task
def add(x, y):
    z = x + y
    print(z)