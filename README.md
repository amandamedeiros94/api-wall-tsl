# TSL Wall [API]

TSL Wall allows users to register, login and write on a wall.

This is the API / admin module of the project created with Python, Django and Django REST framework.

The web module can be found here:

https://github.com/amandamedeiros94/web-wall-tsl

## Config

1.  Install the libs: `pip install -r requirements.txt`

2.  Create the database: `./manage.py migrate`

3.  Create a admin super user: `./manage.py createsuperuser`

4.  Run development server: `./manage.py runserver`

## Deploy

1.  Run: `git push heroku master`

(You need to be signed up for the project at Heroku before)

## Preview

You can see the API running at:

https://api-wall-tsl.herokuapp.com/

and the admin at:

https://api-wall-tsl.herokuapp.com/admin/
