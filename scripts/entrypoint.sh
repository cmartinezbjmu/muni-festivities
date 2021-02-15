#!/bin/sh

set -e

# Creates django static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

# Load default actions
#python manage.py loaddata action_fixtures

#uwsgi --http :$GLOBAL_PORT --master --enable-threads --module main.wsgi
