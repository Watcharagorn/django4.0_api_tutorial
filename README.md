# Django & Celery



## HOW TO RUN
- Run Django Server
```python
python manage.py runserver
```
- Run Redis ( Message Broker )
```python
docker-compose up redis
```
- Run Celery Worker
```python
python -m celery --app apps.mcm worker --pool=solo
```

----------------------
## REF: 
Celery Cst Practice => https://betterprogramming.pub/python-celery-best-practices-ae182730bb81

Celery Config => https://docs.celeryq.dev/en/stable/userguide/configuration.html
