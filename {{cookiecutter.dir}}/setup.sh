#!/bin/bash

echo "Locking dependencies without updating..."
poetry lock --no-update

echo "Starting Poetry shell..."
poetry shell

echo "Installing dependencies (excluding the project root package)..."
poetry install --no-root

echo "Applying database migrations..."
python manage.py migrate

echo "Starting the Django development server..."
python manage.py runserver
