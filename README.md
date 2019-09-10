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

> There are two ways that templates can be created. First, each app to have separete template folder inside app directory. Second, to create generic/global template and create a folder for each app
> To enable global template will change `setting.py` file and define templates directory `DIRS:[os.path.join(BASE_DIR, 'templates')]`
