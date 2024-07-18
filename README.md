# 2024-1-CC4401-1-grupo-3

# Presentation

EstadoBuxef aims to be a website where students, staff, and all people related to FCFM can quickly and effectively report events and incidents that need to be shared, such as available study rooms, open bathrooms, or lunch spaces. \
We are a group of students from the Faculty of Physical and Mathematical Sciences at the University of Chile, aiming to enhance the university experience through a reporting system and its states. Our team members have formed specialized developer teams ranging from design and modeling to testing and backend, and we have successfully developed this platform to promote a harmonious community at Buchef. 
Through these reports, you will be able to discover more about your faculty, such as great places to have lunch, study, or simply relax. Join our community and help us improve university life!


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

## Install Pillow

The project uses Pillow to display the pictures

`pip install Pillow`

## Install Django

The project uses Django 5.0.6. To install it, run:

`pip install django==5.0.6`

Now we can start the server with: `python manage.py runserver`


## Loading initial data into the database

Check that `estadobuxef/migrations` is empty. If it's not, delete everything inside it.

Create migrations for the application:

`python manage.py makemigrations`
`python manage.py makemigrations estadobuxef`

Now import them:

`python manage.py migrate`
`python manage.py migrate estadobuxef`

Load the initial data contained as fixtures:

`python manage.py loaddata initial_data`

