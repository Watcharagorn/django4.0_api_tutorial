import os

from celery import Celery
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@app.task
def error_handler(request, exc, traceback):
    message = "Task {0} raised exception: {1!r}\n{2!r}".format(
        request.id, exc, traceback
    )
    logging.error(message)
    print(message)


@app.task
def success_handler(result):
    message = "Result: {}".format(result)
    logging.error(message)
    print(message)
