#!/bin/bash
echo "ENVIRONMENT : ${environment}"
# yes | python manage.py makemigrations
echo "migration execution..."

python manage.py create_superuser --username admin --email admin@gmail.com --password admin
python manage.py migrate

if [ $? != 0 ] ; 
then
    ispassMigration=false
    echo "---------------- MANUAL LOG: Migration Fail! ----------------"
else
    ispassMigration=true
    echo "---------------- MANUAL LOG: Migration Succeed! ----------------"
fi

if [ "$ispassMigration" = "true" ];
then
    echo "---------------- MANUAL LOG: Starting Server! ----------------"
    # python manage.py collectstatic --clear --noinput
    python manage.py runserver 0.0.0.0:8080
    echo "---------------- MANUAL LOG: StartServer Succeed! ----------------"
else
    echo "---------------- MANUAL LOG: Starting Server Fail! ----------------"
fi
