#!/bin/bash

echo "BUILD START"

# Install dependencies (assuming you have a requirements.txt file)
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

echo "BUILD END"