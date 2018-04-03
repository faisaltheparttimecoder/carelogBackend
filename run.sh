#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate zendesk
python manage.py migrate
nohup /bin/sh  tasks/utilities/task.sh &
gunicorn carelogbackend.wsgi --workers 2
