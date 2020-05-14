#!/bin/sh
set -e

python manage.py makemigrations --check --dry-run --noinput
echo "Migrations: OK"

# Run coverage
coverage erase

pytest app --cov=app --cov-branch --cov-fail-under=95 --cov-report xml --cov-report term-missing:skip-covered --flake8
