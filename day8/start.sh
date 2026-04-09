#!/bin/sh

echo "Waiting for Postgres..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "Postgres is ready"

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn day8.wsgi:application --bind 0.0.0.0:8001

exec "$@"