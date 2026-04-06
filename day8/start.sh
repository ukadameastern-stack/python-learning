#!/bin/bash

echo "Checking Redis..."

redis-cli ping > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Redis not running. Starting Redis..."
    redis-server &
    sleep 1
else
    echo "Redis already running"
fi

echo "Starting Django server..."
python manage.py runserver 8001