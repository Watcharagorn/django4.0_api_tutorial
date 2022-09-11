# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_BROKER_BACKEND = "db+sqlite:///celery.sqlite"
CELERY_RESULT_BACKEND = "django-db"
CELERYD_CONCURRENCY = 1
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"

# If this is True, all tasks will be executed locally by blocking until the task returns.
# Message broker and worker is unnecessary
# only for testing
# CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_ALWAYS_EAGER = False
