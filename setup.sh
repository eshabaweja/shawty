#!/bin/bash

# install from requirements.txt
echo "Installing requirements..."
pip install -r requirements.txt

# To create a fresh database
echo "Deleting old database..."
echo "Creating new database..."
python -m utils/init_db.py

# run main program
echo "Starting application..."
python main.py
