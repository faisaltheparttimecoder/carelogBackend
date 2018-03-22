#!/usr/bin/env bash

# Make all the migration folder
mkdir -p security/migrations
mkdir -p products/migrations
mkdir -p links/migrations


# Create the folder a python executable
touch security/migrations/__init__.py
touch products/migrations/__init__.py
touch links/migrations/__init__.py

# Setup the dev environment ( fill in the details below )
{
  echo 'export DJANGO_SECRET_KEY=<DJANGO-SECRET>'
  echo 'export PIVNET_BASE_URL=<PIVNET_URL>'
  echo 'export ZENDESK_USERNAME=<ZD USERNAME>'
  echo 'export ZENDESK_PASSWORD=<ZD PASSWORD>'

} >> "run_dev.sh"


