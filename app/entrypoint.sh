#!/bin/sh

poetry run python manage.py migrate --noinput
exec "$@"