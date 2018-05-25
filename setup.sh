#!/usr/bin/env bash

# Make all the migration folder
mkdir -p core/migrations
mkdir -p links/migrations
mkdir -p resources/migrations
mkdir -p products/migrations
mkdir -p security/migrations
mkdir -p tasks/migrations
mkdir -p timeline/migrations
mkdir -p zendesk/migrations
mkdir -p environment/migrations
mkdir -p home/migrations

# Create the folder a python executable
touch core/migrations/__init__.py
touch links/migrations/__init__.py
touch resources/migrations/__init__.py
touch products/migrations/__init__.py
touch security/migrations/__init__.py
touch tasks/migrations/__init__.py
touch timeline/migrations/__init__.py
touch zendesk/migrations/__init__.py
touch environment/migrations/__init__.py
touch home/migrations/__init__.py

# Setup the dev environment ( fill in the details below )
{
    echo 'export ENVIRONMENT=<Prod or Dev>'
    echo 'export BASE_URL=<API URL>'
    echo 'export DJANGO_SECRET_KEY=<DJANGO SECRET KEY>'
    echo 'export PIVNET_BASE_URL=<PIVNET BASE URL>'
    echo 'export ZENDESK_BASE_URL=<ZENDESK BASE URL>'
    echo 'export ZENDESK_USERNAME=<ZENDESK USERNAME>'
    echo 'export ZENDESK_PASSWORD=<ZENDESK PASSWORD>'
    echo 'export MYSQL_DATABASE=<MYSQL DATABASE>'
    echo 'export MYSQL_USERNAME=<MYSQL USERNAME>'
    echo 'export MYSQL_PASSWORD=<MYSQL PASSWORD>'
    echo 'export MYSQL_HOST=<MYSQL HOST>'
    echo 'export MYSQL_PORT=<MYSQL PORT>'
    echo 'export ADMIN_PASS=<DJANGO ADMIN PASS>'
    echo 'export GOOGLE_CLIENT_SECRET=<GOOGLE CLIENT SECRET>'
    echo 'export GOOGLE_CLIENT_ID=<GOOGLE CLIENT ID>'
    echo 'export GOOGLE_WHITELIST_DOMAIN=<GOOGLE WHITELIST DOMAIN>'
    echo 'export SOCIAL_AUTH_KEY=<SOCIAL AUTH KEY>'
    echo 'export SOCIAL_AUTH_SECRET=<SOCIAL AUTH SECRET>'
    echo 'export SOCIAL_AUTH_BACKEND=<SOCIAL AUTH BACKEND>'
    echo 'export DJANGO_LOG_LEVEL=<INFO OR DEBUG>'

} >> "run_dev.sh"


