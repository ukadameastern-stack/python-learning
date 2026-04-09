#!/bin/bash

if [ ! -f .env ]; then
  echo "❌ .env file not found!"
  exit 1
fi

set -e

docker compose down
docker compose build
docker compose up -d

docker compose exec web python manage.py migrate

echo "📜 Showing logs..."
# docker compose logs -f web