#!/bin/bash

# exit when any command fails
set -e

echo "ENVIRONMENT : ${environment}"
python3 -u rogue.py './config/settings/template.py' "$PROJECT_CONFIG" ${environment}
python manage.py create_superuser --username admin --email admin@gmail.com --password admin
python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py runserver 0.0.0.0:8080