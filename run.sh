#!/usr/bin/env bash
# Make all the migration folder
mkdir -p core/migrations
mkdir -p links/migrations
mkdir -p products/migrations
mkdir -p security/migrations
mkdir -p tasks/migrations
mkdir -p timeline/migrations
mkdir -p zendesk/migrations

# Create the folder a python executable
touch core/migrations/__init__.py
touch links/migrations/__init__.py
touch products/migrations/__init__.py
touch security/migrations/__init__.py
touch tasks/migrations/__init__.py
touch timeline/migrations/__init__.py
touch zendesk/migrationstouch/__init__.py

# Start the API Web Server
python manage.py makemigrations zendesk
python manage.py migrate zendesk
python manage.py makemigrations
python manage.py migrate
nohup /bin/sh  tasks/utilities/task.sh &
gunicorn carelogbackend.wsgi --workers 2
