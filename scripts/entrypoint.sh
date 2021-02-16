#!/bin/sh

set -e

# Migrate database
python manage.py migrate

# Load default festivities
python manage.py loaddata festivities/utils/fixtures

# Start Django app
python manage.py runserver 0.0.0.0:8000
