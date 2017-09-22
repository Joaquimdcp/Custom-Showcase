#!/bin/sh

# Wait for services to start (pg and es)
sleep 10

# Create and run migrations when needed
python3 manage.py makemigrations api
python3 manage.py migrate

# Ensure admin exists
USER="admin"
PASS="pass"
MAIL="admin@8wires.com"
script="
from api.models import User;

username = '$USER';
password = '$PASS';
email    = '$MAIL';

if User.objects.filter(email=email).count()==0:
    User.objects.create_superuser(username, email, password, first_name='Admin', last_name='Overlord');
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | python3 manage.py shell

script="
from api.search_model import search;

search.create_index( ignore = 400 )
print('Search index created.');
"
printf "$script" | python3 manage.py shell

# Run the server
python3 manage.py runserver 0:8000

