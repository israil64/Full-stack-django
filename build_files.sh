#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Debugging output
echo "Starting build_files.sh script..."
echo "Current directory: $(pwd)"
echo "Listing contents:"
ls -al

# Activate the virtual environment (Windows)
echo "Activating virtual environment..."
source .venv/Scripts/activate || { echo "Failed to activate virtual environment"; exit 1; }

# Check if pip is available
which pip || { echo "pip not found"; exit 1; }
pip --version || { echo "Failed to get pip version"; exit 1; }

# Install dependencies
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

# Run database migrations
python manage.py migrate || { echo "Failed to run migrations"; exit 1; }

# Collect static files
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }
