#!/bin/sh

# Wait for services to start (pg and es)
sleep 10

# Create and run migrations when needed
python3 manage.py makemigrations thumbnail
python3 manage.py makemigrations api
python3 manage.py migrate

# Run the server
python3 manage.py runserver 0:8000

