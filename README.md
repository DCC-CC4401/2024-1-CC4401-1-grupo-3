# 2024-1-CC4401-1-grupo-3

# Development

## Clone repository

`git clone https://github.com/DCC-CC4401/2024-1-CC4401-1-grupo-3.git`

Go to repository directory: `cd 2024-1-CC4401-1-grupo-3`

## Create virtual environment

`python -m venv venv`

## Activate virtual environment

Windows:

`venv/Scripts/activate`

Linux/Mac:

`source venv/bin/activate`

## Install Django

`pip install django`

Now we can start the server with: `python manage.py runserver`

## Loading initial data into the database

Check that `estadobuxef/migrations` is empty. If it's not, delete everything inside it.

Create migrations for the application:

`python manage.py makemigrations`

Now import them:

`python manage.py migrate`

Load the initial data contained as fixtures:

`python manage.py loaddata initial_data`