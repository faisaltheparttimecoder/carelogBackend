#!/usr/bin/env bash
# Make all the migration folder
mkdir -p core/migrations
mkdir -p links/migrations
mkdir -p products/migrations
mkdir -p security/migrations
mkdir -p tasks/migrations
mkdir -p timeline/migrations
mkdir -p zendesk/migrations
mkdir -p environment/migrations

# Create the folder a python executable
touch core/migrations/__init__.py
touch links/migrations/__init__.py
touch products/migrations/__init__.py
touch security/migrations/__init__.py
touch tasks/migrations/__init__.py
touch timeline/migrations/__init__.py
touch zendesk/migrations/__init__.py
touch environment/migrations/__init__.py
touch team/migrations/__init__.py

# Start the API Web Server
python manage.py makemigrations zendesk
python manage.py migrate zendesk
python manage.py makemigrations timeline
python manage.py migrate timeline
python manage.py makemigrations tasks
python manage.py migrate tasks
python manage.py makemigrations security
python manage.py migrate security
python manage.py makemigrations products
python manage.py migrate products
python manage.py makemigrations links
python manage.py migrate links
python manage.py makemigrations environment
python manage.py migrate environment
python manage.py makemigrations team
python manage.py migrate team
python manage.py makemigrations
python manage.py migrate
nohup /bin/sh  tasks/utilities/task.sh &
gunicorn carelogbackend.wsgi --workers 2
