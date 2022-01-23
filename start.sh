#!/usr/bin/env bash

python manage.py makemigrations
# python manage.py migrate
python manage.py migrate --run-syncdb
echo "server running at port 8000"
echo "Author = $AUTHOR"
python manage.py runserver 0.0.0.0:8000
