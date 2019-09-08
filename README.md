# Voting App

Requirments

1. Django
2. Docker

`sudo docker-compose run web django-admin startproject src .`
`sudo docker-compose run web python manage.py startapp vote`
`docker-compose run web python manage.py runserver 0.0.0.0:8000`
`docker-compose run web python manage.py migrate`
`docker-compose run web python manage.py makemigrations vote`
`docker-compose run web python manage.py createsuperuser`
`docker-compose build`
