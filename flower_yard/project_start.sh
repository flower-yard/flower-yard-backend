#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python download_data.py
python manage.py runserver 0:8000