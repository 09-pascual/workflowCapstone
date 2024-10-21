#!/bin/bash

rm db.sqlite3
rm -rf ./workflowapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations workflowapi
python3 manage.py migrate workflowapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

